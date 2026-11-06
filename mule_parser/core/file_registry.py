from __future__ import annotations

import hashlib
import posixpath
import urllib.parse
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def normalize_path(path: str) -> str:
    p = (path or "").strip().replace("\\", "/")
    p = urllib.parse.unquote(p)
    low = p.lower()
    for prefix in ("classpath://", "file://"):
        if low.startswith(prefix):
            p = p[len(prefix):]
            break
    p = p.split("?", 1)[0].split("#", 1)[0]
    p = posixpath.normpath("/" + p).lstrip("/")
    return "" if p == "." else p


@dataclass
class FileRecord:
    path: str
    normalized_path: str
    size_bytes: int
    compressed_size: int
    extension: str
    crc: str
    last_modified: str
    source: str
    archive_path: str


class FileRegistryResolver:
    def __init__(self, files: list[FileRecord], archive_path: Path | None = None):
        self.files = files
        self.archive_path = str(archive_path) if archive_path else ""
        self.by_path: dict[str, FileRecord] = {}
        self.by_filename: dict[str, list[FileRecord]] = {}
        self.by_basename: dict[str, list[FileRecord]] = {}
        self._text_cache: dict[str, str] = {}
        self._bytes_cache: dict[str, bytes] = {}
        self.resolved_reads = 0
        self.failed_reads = 0
        self.resolution_attempts: list[dict[str, Any]] = []
        self.unresolved: list[dict[str, Any]] = []
        self.duplicates: list[dict[str, Any]] = []
        for f in files:
            self.by_path[f.normalized_path] = f
            self.by_filename.setdefault(Path(f.normalized_path).name.lower(), []).append(f)
            self.by_basename.setdefault(Path(f.normalized_path).stem.lower(), []).append(f)
        for name, entries in self.by_filename.items():
            if len(entries) > 1:
                self.duplicates.append({"name": name, "paths": [e.normalized_path for e in entries]})

    @classmethod
    def from_source(cls, source: str, project_root: Path | None = None) -> "FileRegistryResolver":
        p = Path(source.strip())
        if p.is_file() and p.suffix.lower() in {".jar", ".zip"} and zipfile.is_zipfile(p):
            files = build_file_registry_from_archive(p)
            return cls(files, archive_path=p)
        root = project_root or (p if p.is_dir() else p.parent)
        files = build_file_registry_from_filesystem(root)
        return cls(files, archive_path=None)

    def resolve(self, requested_path: str, *, relative_to: str = "") -> tuple[FileRecord | None, list[str], str]:
        attempts: list[str] = []
        req = normalize_path(requested_path)
        rel = normalize_path(relative_to)
        candidates = [req]
        if rel:
            base = normalize_path(str(Path(rel).parent / req))
            if base not in candidates:
                candidates.append(base)
        if req.startswith("META-INF/"):
            stripped = req.split("META-INF/", 1)[-1]
            if stripped not in candidates:
                candidates.append(stripped)
        for cand in list(candidates):
            candidates.extend(_candidate_aliases(cand))
        seen = set()
        ordered = []
        for c in candidates:
            if c and c not in seen:
                seen.add(c)
                ordered.append(c)
        for cand in ordered:
            attempts.append(f"manifest:{cand}")
            if cand in self.by_path:
                self.resolution_attempts.append({"requested_path": requested_path, "normalized_path": req, "attempts": attempts, "resolved": cand})
                return self.by_path[cand], attempts, ""
        name = Path(req).name.lower()
        by_name = self.by_filename.get(name, [])
        if len(by_name) == 1:
            hit = by_name[0]
            attempts.append(f"filename:{name}")
            self.resolution_attempts.append({"requested_path": requested_path, "normalized_path": req, "attempts": attempts, "resolved": hit.normalized_path})
            return hit, attempts, ""
        reason = "not found in manifest"
        miss = {"requested_path": requested_path, "normalized_path": req, "resolution_attempts": attempts, "failure_reason": reason}
        self.unresolved.append(miss)
        self.resolution_attempts.append({**miss, "resolved": ""})
        return None, attempts, reason

    def read_text(self, requested_path: str, *, relative_to: str = "") -> tuple[str, FileRecord | None, list[str], str]:
        rec, attempts, err = self.resolve(requested_path, relative_to=relative_to)
        if rec is None:
            self.failed_reads += 1
            return "", None, attempts, err
        key = rec.normalized_path
        if key in self._text_cache:
            self.resolved_reads += 1
            return self._text_cache[key], rec, attempts, ""
        try:
            raw = self.read_bytes_by_record(rec)
            text = raw.decode("utf-8", errors="replace")
            self._text_cache[key] = text
            self.resolved_reads += 1
            return text, rec, attempts, ""
        except Exception as exc:
            self.failed_reads += 1
            msg = str(exc)
            self.unresolved.append({
                "requested_path": requested_path,
                "normalized_path": normalize_path(requested_path),
                "resolution_attempts": attempts,
                "failure_reason": msg,
            })
            return "", rec, attempts, msg

    def read_bytes_by_record(self, rec: FileRecord) -> bytes:
        key = rec.normalized_path
        if key in self._bytes_cache:
            return self._bytes_cache[key]
        if rec.source == "jar" and self.archive_path:
            with zipfile.ZipFile(self.archive_path, "r") as zf:
                raw = zf.read(rec.path)
        else:
            raw = Path(rec.path).read_bytes()
        self._bytes_cache[key] = raw
        return raw

    def metadata_for(self, requested_path: str, *, relative_to: str = "") -> dict[str, Any]:
        rec, attempts, err = self.resolve(requested_path, relative_to=relative_to)
        if rec is None:
            return {
                "path": normalize_path(requested_path),
                "exists": False,
                "size_bytes": None,
                "checksum": "",
                "source_archive_path": self.archive_path,
                "resolved_from": "",
                "resolution_method": attempts[-1] if attempts else "",
                "resolution_attempts": attempts,
                "error": err,
            }
        return {
            "path": rec.normalized_path,
            "exists": True,
            "size_bytes": rec.size_bytes,
            "checksum": rec.crc,
            "source_archive_path": rec.archive_path,
            "resolved_from": "jar_manifest" if rec.source == "jar" else "filesystem",
            "resolution_method": attempts[-1] if attempts else "",
            "resolution_attempts": attempts,
            "error": "",
        }

    def to_ir_section(self) -> dict[str, Any]:
        total_size = sum(f.size_bytes for f in self.files)
        return {
            "files": [f.__dict__ for f in self.files],
            "unresolved": self.unresolved,
            "duplicates": self.duplicates,
            "stats": {
                "total_files": len(self.files),
                "resolved_reads": self.resolved_reads,
                "failed_reads": self.failed_reads,
                "duplicate_names": len(self.duplicates),
                "total_size_bytes": total_size,
            },
        }

    def validate(self, raw_output: Any) -> dict[str, Any]:
        refs: list[str] = []
        refs.extend(getattr(raw_output, "mule_config_files", []) or [])
        refs.extend(getattr(raw_output, "property_files", []) or [])
        refs.extend([(d.resource_path or d.file) for d in (getattr(raw_output, "dataweave", []) or []) if (d.resource_path or d.file)])
        dangling = []
        for ref in refs:
            rec, _, _ = self.resolve(ref)
            if rec is None:
                dangling.append(ref)
        empty_files = [f.normalized_path for f in self.files if f.size_bytes == 0]
        return {
            "unresolved_references": sorted(set(dangling)),
            "dangling_references": sorted(set(dangling)),
            "duplicate_paths": self.duplicates,
            "empty_files": sorted(set(empty_files)),
            "corrupted_entries": [],
        }


def build_file_registry_from_archive(archive_path: Path) -> list[FileRecord]:
    files: list[FileRecord] = []
    with zipfile.ZipFile(archive_path, "r") as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            norm = normalize_path(info.filename)
            dt = datetime(*info.date_time, tzinfo=timezone.utc).isoformat()
            files.append(
                FileRecord(
                    path=info.filename.replace("\\", "/"),
                    normalized_path=norm,
                    size_bytes=info.file_size,
                    compressed_size=info.compress_size,
                    extension=Path(norm).suffix.lower(),
                    crc=f"{info.CRC:08x}",
                    last_modified=dt,
                    source="jar",
                    archive_path=str(archive_path),
                )
            )
    return files


def build_file_registry_from_filesystem(root: Path) -> list[FileRecord]:
    files: list[FileRecord] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        try:
            stat = p.stat()
            raw = p.read_bytes()
        except Exception:
            continue
        rel = normalize_path(str(p.relative_to(root)))
        files.append(
            FileRecord(
                path=str(p),
                normalized_path=rel,
                size_bytes=stat.st_size,
                compressed_size=stat.st_size,
                extension=p.suffix.lower(),
                crc=hashlib.sha256(raw).hexdigest(),
                last_modified=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                source="filesystem",
                archive_path=str(root),
            )
        )
    return files


def _candidate_aliases(norm: str) -> list[str]:
    base = norm.lstrip("/")
    aliases = [base]
    prefixes = [
        "src/main/resources/",
        "src/main/mule/",
        "src/test/resources/",
        "META-INF/mule-src/",
        "api/",
    ]
    for pref in prefixes:
        aliases.append(normalize_path(pref + base))
    return aliases

