"""Preserve and verify the three local research collections without changing them."""
import argparse
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT_NAMES = (
    "akto-research-2026-10-06",
    "evaluation-datasets-2026-10-06",
    "evaluation-review-2026-10-06",
)
SKIP = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
TOKEN = re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{10,}|github_pat_[A-Za-z0-9_]{10,})")
REDACT_PATH = "local-materials/akto-research-2026-10-06/evidence/github/details/files-683.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def inventory(workspace):
    files, clones, excluded = [], [], []
    for name in ROOT_NAMES:
        root = workspace / "local-materials" / name
        if not root.is_dir():
            raise FileNotFoundError(root)
        for directory, dirs, names in os.walk(root):
            directory = Path(directory)
            if ".git" in dirs or ".git" in names:
                clones.append(directory)
                dirs[:] = []
                continue
            for name in list(dirs):
                if name in SKIP or name.startswith(".venv"):
                    excluded.append((directory / name).relative_to(workspace).as_posix())
                    dirs.remove(name)
            files.extend(directory / name for name in names)
    return sorted(files), sorted(clones), sorted(excluded)


def build(workspace, repo, archive):
    manifest_path = archive / "MANIFEST.json"
    if manifest_path.exists():
        raise RuntimeError("Archive already exists; use verify instead of overwriting it")
    files, clones, excluded = inventory(workspace)
    known = {}
    for raw in git(repo, "ls-files", "-z", "--", "docs").split(b"\0"):
        if raw:
            rel = raw.decode("utf-8")
            path = repo / rel
            if path.is_file():
                known.setdefault(sha(path.read_bytes()), (rel, "identity"))
    entries = []
    for path in files:
        source = path.relative_to(workspace).as_posix()
        data = path.read_bytes()
        original_hash = sha(data)
        redactions = 0
        if source == REDACT_PATH:
            data, redactions = TOKEN.subn(b"[REDACTED_TOKEN_EXAMPLE]", data)
        digest = sha(data)
        if digest in known:
            storage, encoding = known[digest]
            disposition = "existing-identical-file"
        else:
            target = archive / "files" / source
            encoding = "gzip" if len(data) > 5 * 1024 * 1024 and path.suffix.lower() in {".json", ".jsonl", ".html", ".csv", ".txt", ".md", ".log"} else "identity"
            if encoding == "gzip":
                target = target.with_name(target.name + ".gz")
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise FileExistsError(target)
            if encoding == "gzip":
                with target.open("wb") as output:
                    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as stream:
                        stream.write(data)
            elif redactions:
                target.write_bytes(data)
            else:
                shutil.copyfile(path, target)
            storage = target.relative_to(repo).as_posix()
            known[digest] = (storage, encoding)
            disposition = "archived"
        stored = repo / storage
        entries.append({"source": source, "original_bytes": path.stat().st_size,
                        "original_sha256": original_hash, "storage": storage,
                        "encoding": encoding, "content_sha256": digest,
                        "stored_sha256": sha(stored.read_bytes()), "disposition": disposition,
                        "token_example_redactions": redactions})
    snapshots = []
    for number, clone in enumerate(clones, 1):
        status = git(clone, "status", "--porcelain").decode("utf-8").strip()
        if status:
            raise RuntimeError("Source checkout has unarchived changes: " + str(clone))
        extra = git(clone, "ls-files", "--others", "--ignored", "--exclude-standard", "-z").decode("utf-8").split("\0")
        noncache = [p for p in extra if p and not any(part in SKIP or part.startswith(".venv") for part in Path(p).parts)]
        if noncache:
            raise RuntimeError("Source checkout has ignored research files: " + str(clone))
        records = []
        for item in git(clone, "ls-tree", "-r", "-z", "HEAD").split(b"\0"):
            if item:
                meta, name = item.split(b"\t", 1)
                mode, kind, oid = meta.decode().split()
                records.append({"path": name.decode("utf-8"), "mode": mode, "type": kind, "object": oid})
        tree_file = archive / "source-trees" / f"{number:02d}-{clone.name}.json"
        write_json(tree_file, records)
        snapshots.append({"source": clone.relative_to(workspace).as_posix(),
                          "remote": git(clone, "remote", "get-url", "origin").decode().strip(),
                          "commit": git(clone, "rev-parse", "HEAD").decode().strip(),
                          "tree": git(clone, "rev-parse", "HEAD^{tree}").decode().strip(),
                          "clean": True, "tracked_entries": len(records),
                          "tree_inventory": tree_file.relative_to(repo).as_posix(),
                          "tree_inventory_sha256": sha(tree_file.read_bytes()),
                          "ignored_cache_files": sum(bool(p) for p in extra)})
    write_json(manifest_path, {"date": "2026-10-06", "scope": list(ROOT_NAMES),
                              "files": entries, "source_repositories": snapshots,
                              "excluded_runtime_directories": excluded})
    verify(repo, archive, workspace)


def verify(repo, archive, workspace=None):
    manifest = json.loads((archive / "MANIFEST.json").read_text(encoding="utf-8"))
    errors = []
    for entry in manifest["files"]:
        path = (repo / entry["storage"]).resolve()
        if not path.is_relative_to(repo.resolve()):
            raise ValueError("Storage path leaves repository")
        stored = path.read_bytes()
        data = gzip.decompress(stored) if entry["encoding"] == "gzip" else stored
        if sha(stored) != entry["stored_sha256"] or sha(data) != entry["content_sha256"]:
            errors.append(entry["source"])
        if workspace is not None and sha((workspace / entry["source"]).read_bytes()) != entry["original_sha256"]:
            errors.append("source changed: " + entry["source"])
    for entry in manifest["source_repositories"]:
        if sha((repo / entry["tree_inventory"]).read_bytes()) != entry["tree_inventory_sha256"]:
            errors.append(entry["source"])
    if workspace is not None:
        files, clones, _ = inventory(workspace)
        if {p.relative_to(workspace).as_posix() for p in files} != {e["source"] for e in manifest["files"]}:
            errors.append("source file coverage differs")
        if {p.relative_to(workspace).as_posix() for p in clones} != {e["source"] for e in manifest["source_repositories"]}:
            errors.append("source repository coverage differs")
    print(json.dumps({"research_files": len(manifest["files"]),
                      "source_repositories": len(manifest["source_repositories"]), "errors": errors}, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("build", "verify"))
    parser.add_argument("--workspace", type=Path)
    args = parser.parse_args()
    archive = Path(__file__).resolve().parent.parent
    repo = archive.parents[2]
    if args.mode == "build":
        if args.workspace is None:
            parser.error("build requires --workspace")
        build(args.workspace.resolve(), repo, archive)
    else:
        verify(repo, archive, args.workspace.resolve() if args.workspace else None)
