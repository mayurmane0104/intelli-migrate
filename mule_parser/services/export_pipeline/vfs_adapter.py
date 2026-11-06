"""
services/export_pipeline/vfs_adapter.py — VirtualFileSystem Compatibility Adapter.

Guarantees seamless enumeration and interaction with any VirtualFileSystem
variant or object across all generators, exporters, and gate runners.
"""
from __future__ import annotations

import logging
from typing import Any, Iterator
from mule_parser.services.export_pipeline.vfs import VFile, VirtualFileSystem

logger = logging.getLogger(__name__)


def enumerate_vfs_files(vfs: Any, prefix: str = "") -> list[VFile]:
    """Inspect and extract VFile entries from any VFS implementation.
    
    Tries canonical methods in order without assuming any single method name:
      1. files()
      2. list_files()
      3. get_files()
      4. entries()
      5. iter_files()
      6. list_paths() + read()
      7. __iter__()
      8. _files dictionary fallback
    """
    if vfs is None:
        return []

    # 1. files()
    if hasattr(vfs, "files") and callable(getattr(vfs, "files")):
        try:
            res = vfs.files(prefix)
            if isinstance(res, (list, tuple)):
                return list(res)
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.files(%r) raised %s", prefix, exc)

    # 2. list_files()
    if hasattr(vfs, "list_files") and callable(getattr(vfs, "list_files")):
        try:
            res = vfs.list_files(prefix)
            if isinstance(res, (list, tuple)):
                return list(res)
            elif hasattr(res, "__iter__"):
                return list(res)
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.list_files(%r) raised %s", prefix, exc)

    # 3. get_files()
    if hasattr(vfs, "get_files") and callable(getattr(vfs, "get_files")):
        try:
            res = vfs.get_files(prefix)
            if isinstance(res, (list, tuple)):
                return list(res)
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.get_files(%r) raised %s", prefix, exc)

    # 4. entries()
    if hasattr(vfs, "entries") and callable(getattr(vfs, "entries")):
        try:
            res = vfs.entries(prefix)
            if isinstance(res, (list, tuple)):
                return list(res)
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.entries(%r) raised %s", prefix, exc)

    # 5. iter_files()
    if hasattr(vfs, "iter_files") and callable(getattr(vfs, "iter_files")):
        try:
            return list(vfs.iter_files(prefix))
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.iter_files(%r) raised %s", prefix, exc)

    # 6. list_paths() + read()
    if hasattr(vfs, "list_paths") and callable(getattr(vfs, "list_paths")):
        try:
            paths = vfs.list_paths(prefix)
            out: list[VFile] = []
            for p in paths:
                vfile = get_vfs_file(vfs, p)
                if vfile:
                    out.append(vfile)
            return out
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.list_paths(%r) raised %s", prefix, exc)

    # 7. __iter__()
    if hasattr(vfs, "__iter__") and callable(getattr(vfs, "__iter__")):
        try:
            items = list(vfs)
            out = []
            for item in items:
                if isinstance(item, VFile):
                    out.append(item)
                elif isinstance(item, str):
                    vf = get_vfs_file(vfs, item)
                    if vf:
                        out.append(vf)
            if out:
                return out
        except Exception as exc:
            logger.debug("VFSAdapter: vfs.__iter__() raised %s", exc)

    # 8. _files attribute fallback
    if hasattr(vfs, "_files"):
        try:
            raw_files = getattr(vfs, "_files")
            if isinstance(raw_files, dict):
                out = []
                for p, val in sorted(raw_files.items()):
                    if prefix and not p.startswith(prefix):
                        continue
                    if isinstance(val, VFile):
                        out.append(val)
                    elif isinstance(val, (str, bytes)):
                        content = val.encode("utf-8") if isinstance(val, str) else val
                        out.append(VFile(path=p, content=content))
                return out
        except Exception as exc:
            logger.debug("VFSAdapter: vfs._files access raised %s", exc)

    logger.warning("VFSAdapter: Unable to enumerate files from VFS object of type %s", type(vfs).__name__)
    return []


def get_vfs_file(vfs: Any, path: str) -> VFile | None:
    """Retrieve a single VFile by path from any VFS implementation."""
    if vfs is None:
        return None

    if hasattr(vfs, "read") and callable(getattr(vfs, "read")):
        try:
            res = vfs.read(path)
            if isinstance(res, VFile):
                return res
            elif isinstance(res, (str, bytes)):
                content = res.encode("utf-8") if isinstance(res, str) else res
                return VFile(path=path, content=content)
        except Exception:
            pass

    if hasattr(vfs, "get") and callable(getattr(vfs, "get")):
        try:
            res = vfs.get(path)
            if isinstance(res, VFile):
                return res
            elif isinstance(res, (str, bytes)):
                content = res.encode("utf-8") if isinstance(res, str) else res
                return VFile(path=path, content=content)
        except Exception:
            pass

    if hasattr(vfs, "_files") and isinstance(getattr(vfs, "_files"), dict):
        raw = getattr(vfs, "_files").get(path)
        if isinstance(raw, VFile):
            return raw
        elif isinstance(raw, (str, bytes)):
            content = raw.encode("utf-8") if isinstance(raw, str) else raw
            return VFile(path=path, content=content)

    return None


class VFSAdapter:
    """Compatibility Wrapper around any VirtualFileSystem object."""

    def __init__(self, inner: Any) -> None:
        self._inner = inner if inner is not None else VirtualFileSystem()

    def files(self, prefix: str = "") -> list[VFile]:
        return enumerate_vfs_files(self._inner, prefix)

    def list_files(self, prefix: str = "") -> list[VFile]:
        return self.files(prefix)

    def get_files(self, prefix: str = "") -> list[VFile]:
        return self.files(prefix)

    def entries(self, prefix: str = "") -> list[VFile]:
        return self.files(prefix)

    def list_paths(self, prefix: str = "") -> list[str]:
        return [f.path for f in self.files(prefix)]

    def read(self, path: str) -> VFile | None:
        return get_vfs_file(self._inner, path)

    def exists(self, path: str) -> bool:
        if hasattr(self._inner, "exists") and callable(getattr(self._inner, "exists")):
            return self._inner.exists(path)
        return get_vfs_file(self._inner, path) is not None

    def write(self, path: str, content: bytes | str, **kwargs: Any) -> VFile:
        if hasattr(self._inner, "write") and callable(getattr(self._inner, "write")):
            return self._inner.write(path, content, **kwargs)
        payload = content.encode("utf-8") if isinstance(content, str) else bytes(content)
        vfile = VFile(path=path, content=payload, **kwargs)
        if hasattr(self._inner, "_files") and isinstance(getattr(self._inner, "_files"), dict):
            getattr(self._inner, "_files")[path] = vfile
        return vfile

    def root_with(self, root: str) -> "VFSAdapter":
        if hasattr(self._inner, "root_with") and callable(getattr(self._inner, "root_with")):
            return VFSAdapter(self._inner.root_with(root))
        vfs = VirtualFileSystem()
        prefix = root.rstrip("/") + "/"
        for v in self.files():
            vfs.write(prefix + v.path, v.content, role=v.role, generator=v.generator, metadata=dict(v.metadata))
        return VFSAdapter(vfs)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._inner, name)

    def __iter__(self) -> Iterator[VFile]:
        return iter(self.files())

    def __len__(self) -> int:
        return len(self.files())
