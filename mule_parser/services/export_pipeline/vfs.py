"""
services/export_pipeline/vfs.py - In-memory hierarchical file store.

Contract
--------
Generators write into the VFS, never to disk. Format adapters MAY rearrange
files in the VFS but never read or write actual files. Final packaging
(ZIP, S3 push, Git push) consumes the VFS at the end.

Path safety
-----------
* paths are POSIX-style ("/")
* leading slashes are stripped
* "..", "//", and absolute paths (e.g. "C:\\foo") are rejected
* directories are implicit (derived from file paths) - no separate type

Determinism
-----------
* writes are stored in an ordered dict keyed by path
* `files()` returns entries sorted lexicographically
* same inputs -> same byte-identical ZIP
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


_INVALID_PATH = re.compile(r"(^|/)\.\.(/|$)")


def normalise_path(path: str) -> str:
    """Validate + normalise a path. Raises ValueError on unsafe input."""
    if not isinstance(path, str):
        raise ValueError(f"path must be a string, got {type(path).__name__}")
    p = path.replace("\\", "/").strip()
    if not p:
        raise ValueError("path cannot be empty")
    # Reject Windows-style absolute paths and POSIX absolute paths.
    if re.match(r"^[A-Za-z]:/", p) or p.startswith("//"):
        raise ValueError(f"absolute paths are not allowed: {path!r}")
    p = p.lstrip("/")
    if _INVALID_PATH.search(p):
        raise ValueError(f"path traversal segments are not allowed: {path!r}")
    # Collapse double slashes that may have leaked in.
    while "//" in p:
        p = p.replace("//", "/")
    if not p:
        raise ValueError(f"path is empty after normalisation: {path!r}")
    return p


@dataclass
class VFile:
    """A single in-memory file."""

    path: str
    content: bytes
    role: str = ""               # handler | iac | config | test | doc | boilerplate | data
    generator: str = ""          # which generator emitted this file
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def size(self) -> int:
        return len(self.content)


class VFSError(Exception):
    """Raised on VFS contract violations (unsafe paths, conflicting writes)."""


class VirtualFileSystem:
    """In-memory file store consumed by the export pipeline."""

    def __init__(self) -> None:
        self._files: dict[str, VFile] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def write(
        self,
        path: str,
        content: bytes | str,
        *,
        role: str = "",
        generator: str = "",
        metadata: dict[str, Any] | None = None,
        overwrite: bool = False,
    ) -> VFile:
        """Write a file. Refuses to overwrite unless `overwrite=True`."""
        normalised = normalise_path(path)
        

        payload = content.encode("utf-8") if isinstance(content, str) else bytes(content)
        existing = self._files.get(normalised)
        if existing is not None and not overwrite:
            raise VFSError(
                f"refusing to overwrite {normalised!r} previously written by "
                f"{existing.generator or 'unknown'} (pass overwrite=True to allow)"
            )
        
        # Pre-write collision check (X.py vs X/)
        for existing_path in self._files.keys():
            if existing_path == normalised:
                continue
            # If the new path is a prefix of an existing path (X/ vs X)
            if existing_path.startswith(normalised + "/"):
                raise VFSError(
                    f"path collision: cannot write file {normalised!r} because "
                    f"it is a directory for existing file {existing_path!r}"
                )
            # If an existing path is a prefix of the new path (X vs X/)
            if normalised.startswith(existing_path + "/"):
                raise VFSError(
                    f"path collision: cannot write file {normalised!r} because "
                    f"existing file {existing_path!r} acts as its directory"
                )

        vfile = VFile(
            path=normalised,
            content=payload,
            role=role or (existing.role if existing else ""),
            generator=generator or (existing.generator if existing else ""),
            metadata={**(existing.metadata if existing else {}), **(metadata or {})},
        )
        self._files[normalised] = vfile
        return vfile

    def write_text(self, path: str, content: str, **kwargs: Any) -> VFile:
        return self.write(path, content, **kwargs)

    def write_json(self, path: str, payload: Any, **kwargs: Any) -> VFile:
        import json as _json
        return self.write(path, _json.dumps(payload, indent=2, sort_keys=True, default=str), **kwargs)

    def remove(self, path: str) -> bool:
        normalised = normalise_path(path)
        return self._files.pop(normalised, None) is not None

    def move(self, src: str, dst: str, *, overwrite: bool = False) -> VFile:
        src_n = normalise_path(src)
        dst_n = normalise_path(dst)
        if src_n == dst_n:
            return self._files[src_n]
        if dst_n in self._files and not overwrite:
            raise VFSError(f"cannot move {src_n!r} over existing {dst_n!r}")
        if src_n not in self._files:
            raise VFSError(f"cannot move missing path {src_n!r}")
        v = self._files.pop(src_n)
        moved = VFile(path=dst_n, content=v.content, role=v.role, generator=v.generator, metadata=v.metadata)
        self._files[dst_n] = moved
        return moved

    def exists(self, path: str) -> bool:
        try:
            normalised = normalise_path(path)
        except ValueError:
            return False
        return normalised in self._files

    def read(self, path: str) -> VFile | None:
        normalised = normalise_path(path)
        return self._files.get(normalised)

    def list_paths(self, prefix: str = "") -> list[str]:
        """Return all paths optionally filtered by prefix, sorted ascending."""
        prefix_n = ""
        if prefix:
            prefix_n = normalise_path(prefix).rstrip("/") + "/"
        if not prefix_n:
            return sorted(self._files.keys())
        return sorted(p for p in self._files if p.startswith(prefix_n) or p == prefix_n.rstrip("/"))

    def files(self, prefix: str = "") -> list[VFile]:
        return [self._files[p] for p in self.list_paths(prefix)]

    # ------------------------------------------------------------------
    # Compatibility API aliases & methods
    # ------------------------------------------------------------------

    def list_files(self, prefix: str = "") -> list[VFile]:
        """Canonical compatibility alias for files()."""
        return self.files(prefix)

    def get_files(self, prefix: str = "") -> list[VFile]:
        """Compatibility alias for files()."""
        return self.files(prefix)

    def entries(self, prefix: str = "") -> list[VFile]:
        """Compatibility alias for files()."""
        return self.files(prefix)

    def iter_files(self, prefix: str = ""):
        """Yield VFile instances."""
        for f in self.files(prefix):
            yield f

    def glob(self, pattern: str) -> list[VFile]:
        """Filter files by fnmatch glob pattern."""
        import fnmatch
        return [f for f in self.files() if fnmatch.fnmatch(f.path, pattern)]

    def stat(self, path: str) -> dict[str, Any]:
        """Return file metadata information."""
        f = self.read(path)
        if not f:
            raise VFSError(f"File not found: {path!r}")
        return {
            "path": f.path,
            "size": f.size,
            "role": f.role,
            "generator": f.generator,
            "metadata": f.metadata,
        }

    def walk(self):
        """Directory tree generator matching os.walk behavior for VFS."""
        from collections import defaultdict
        dirs: dict[str, set[str]] = defaultdict(set)
        files_by_dir: dict[str, list[str]] = defaultdict(list)
        for p in self.list_paths():
            parts = p.split("/")
            filename = parts[-1]
            dirname = "/".join(parts[:-1])
            files_by_dir[dirname].append(filename)
            while parts:
                child = parts.pop()
                parent = "/".join(parts)
                if parent != child and child:
                    dirs[parent].add(child)
        for d in sorted(dirs.keys()):
            subdirs = sorted(list(dirs[d]))
            subfiles = sorted(files_by_dir[d])
            yield (d, subdirs, subfiles)

    def __len__(self) -> int:
        return len(self._files)

    def __contains__(self, path: str) -> bool:
        return self.exists(path)

    def __iter__(self):
        for p in self.list_paths():
            yield self._files[p]

    # ------------------------------------------------------------------
    # Bulk operations
    # ------------------------------------------------------------------

    def merge(self, other: "VirtualFileSystem", *, overwrite: bool = False) -> None:
        for v in other.files():
            self.write(
                v.path,
                v.content,
                role=v.role,
                generator=v.generator,
                metadata=dict(v.metadata),
                overwrite=overwrite,
            )

    def root_with(self, root: str) -> "VirtualFileSystem":
        """Return a new VFS with every path prefixed by ``root``."""
        prefix = normalise_path(root).rstrip("/") + "/"
        out = VirtualFileSystem()
        for v in self.files():
            out.write(
                prefix + v.path,
                v.content,
                role=v.role,
                generator=v.generator,
                metadata=dict(v.metadata),
            )
        return out

    def stats(self) -> dict[str, Any]:
        roles: dict[str, int] = {}
        generators_seen: dict[str, int] = {}
        total_bytes = 0
        for v in self.files():
            roles[v.role or "unknown"] = roles.get(v.role or "unknown", 0) + 1
            if v.generator:
                generators_seen[v.generator] = generators_seen.get(v.generator, 0) + 1
            total_bytes += v.size
        return {
            "file_count": len(self._files),
            "total_bytes": total_bytes,
            "by_role": dict(sorted(roles.items())),
            "by_generator": dict(sorted(generators_seen.items())),
        }

    def to_dict(self) -> dict[str, Any]:
        import base64
        return {
            "files": {
                p: {
                    "content_b64": base64.b64encode(v.content).decode("utf-8"),
                    "role": v.role,
                    "generator": v.generator,
                    "metadata": v.metadata,
                }
                for p, v in self._files.items()
            }
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "VirtualFileSystem":
        import base64
        vfs = cls()
        files = data.get("files", {})
        for p, v in files.items():
            content = base64.b64decode(v["content_b64"])
            vfs.write(
                p,
                content,
                role=v.get("role", ""),
                generator=v.get("generator", ""),
                metadata=v.get("metadata", {}),
            )
        return vfs
