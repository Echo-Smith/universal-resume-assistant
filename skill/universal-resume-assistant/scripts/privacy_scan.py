#!/usr/bin/env python3
"""Flag likely sensitive data in text files before a resume is shared.

This is a conservative detector, not proof that a file is safe. Review every match.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TEXT_SUFFIXES = {
    ".csv",
    ".html",
    ".json",
    ".md",
    ".rst",
    ".text",
    ".toml",
    ".tsv",
    ".txt",
    ".yaml",
    ".yml",
}

PATTERNS = {
    "email": re.compile(r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "phone": re.compile(r"(?<!\w)(?:\+?\d[\d ().-]{7,}\d)(?!\w)"),
    "absolute_home_path": re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\\\Users\\\\)[^\s\"']+"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "common_secret": re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\b\s*[:=]\s*[^\s$<{][^\s,;]{5,}"
    ),
}


def iter_files(paths: list[Path]):
    for path in paths:
        if path.is_file():
            yield path
            continue
        if path.is_dir():
            for candidate in sorted(path.rglob("*")):
                if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES:
                    yield candidate


def scan_file(path: Path) -> list[dict[str, object]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return []

    findings: list[dict[str, object]] = []
    for line_number, line in enumerate(lines, start=1):
        for kind, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                findings.append(
                    {
                        "file": str(path),
                        "line": line_number,
                        "kind": kind,
                        "match": match.group(0),
                    }
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    findings = [item for path in iter_files(args.paths) for item in scan_file(path)]
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item['file']}:{item['line']}: {item['kind']}: {item['match']}")
        print(f"Findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
