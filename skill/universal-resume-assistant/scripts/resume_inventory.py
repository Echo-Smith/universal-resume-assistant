#!/usr/bin/env python3
"""Inventory active resume sources and generated outputs."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path


DEFAULT_LOCATIONS = {
    "text": Path("resume/current"),
    "html": Path("output/html"),
    "pdf": Path("output/pdf"),
}


def semantic_key(path: Path) -> str:
    stem = path.stem
    suffixes = ("-文字稿", "-定向简历", "-通用简历")
    changed = True
    while changed:
        changed = False
        for suffix in suffixes:
            if stem.endswith(suffix):
                stem = stem[: -len(suffix)]
                changed = True
                break
    return stem


def collect(root: Path, relative: Path, extension: str) -> list[Path]:
    directory = root / relative
    if not directory.exists():
        return []
    return sorted(
        path.relative_to(root)
        for path in directory.glob(f"*{extension}")
        if path.is_file()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Workspace root; defaults to the current directory.",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    files = {
        kind: collect(root, path, extension)
        for kind, path, extension in (
            ("text", DEFAULT_LOCATIONS["text"], ".md"),
            ("html", DEFAULT_LOCATIONS["html"], ".html"),
            ("pdf", DEFAULT_LOCATIONS["pdf"], ".pdf"),
        )
    }

    grouped: dict[str, dict[str, list[Path]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for kind, paths in files.items():
        for path in paths:
            grouped[semantic_key(path)][kind].append(path)

    print(f"Workspace: {root}")
    print(f"Targets: {len(grouped)}")
    print()

    incomplete = False
    for key in sorted(grouped):
        print(key)
        for kind in ("text", "html", "pdf"):
            paths = grouped[key].get(kind, [])
            if paths:
                for path in paths:
                    print(f"  {kind.upper()}: {path}")
            else:
                print(f"  {kind.upper()}: MISSING")
                incomplete = True
        print()

    if not grouped:
        print("No active resume assets found in the default locations.")
        return 1
    if incomplete:
        print("Status: active asset set is incomplete.")
        return 2
    print("Status: every target has text, HTML, and PDF assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
