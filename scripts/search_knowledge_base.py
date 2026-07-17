#!/usr/bin/env python3
"""Minimal local knowledge-base search for Founder OS docs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIRS = ["docs", "evidence", "exports"]
TEXT_EXTENSIONS = {".md", ".txt"}


@dataclass(frozen=True)
class Match:
    source_path: str
    excerpt: str
    confidence: str


@dataclass(frozen=True)
class SearchResult:
    query: str
    matches: list[Match]
    answer: str
    gaps: list[str]


def normalize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_/-]+", text.lower())


def iter_files(target_dirs: list[str]) -> list[Path]:
    files: list[Path] = []

    for directory in target_dirs:
        base = ROOT / directory
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
                files.append(path)

    return sorted(files)


def build_excerpt(text: str, keyword: str) -> str:
    for line in text.splitlines():
        if keyword.lower() in line.lower():
            return line.strip()

    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped[:180]

    return ""


def confidence_for(score: int) -> str:
    if score >= 3:
        return "high"
    if score == 2:
        return "medium"
    return "low"


def search(query: str, target_dirs: list[str], limit: int) -> SearchResult:
    keywords = normalize(query)
    matches: list[tuple[int, Match]] = []

    for path in iter_files(target_dirs):
        text = path.read_text(encoding="utf-8")
        haystack = text.lower()
        score = sum(1 for keyword in keywords if keyword in haystack)
        path_str = str(path.relative_to(ROOT))

        if score == 0:
            continue

        if path_str.startswith("docs/"):
            score += 2
        if "permissions-policy" in path_str:
            score += 3

        excerpt = build_excerpt(text, keywords[0]) if keywords else ""
        matches.append(
            (
                score,
                Match(
                    source_path=path_str,
                    excerpt=excerpt,
                    confidence=confidence_for(score),
                ),
            )
        )

    matches.sort(key=lambda item: (-item[0], item[1].source_path))
    selected = [match for _, match in matches[:limit]]

    if selected:
        answer = (
            f"{len(selected)} source(s) trouvee(s) pour la requete. "
            f"La meilleure source est {selected[0].source_path}."
        )
        gaps: list[str] = []
    else:
        answer = "Aucune source pertinente trouvee dans les dossiers cibles."
        gaps = ["A verifier : elargir les mots-cles ou ajouter d'autres dossiers cibles."]

    return SearchResult(query=query, matches=selected, answer=answer, gaps=gaps)


def to_text(result: SearchResult) -> str:
    if result.matches:
        blocks = []
        for match in result.matches:
            blocks.append(
                "\n".join(
                    [
                        f"- source: {match.source_path}",
                        f"  confidence: {match.confidence}",
                        f"  excerpt: {match.excerpt}",
                    ]
                )
            )
        match_lines = "\n".join(blocks)
    else:
        match_lines = "- aucune"

    gap_lines = "\n".join(f"- {gap}" for gap in result.gaps) or "- aucune"

    return (
        f"Query :\n{result.query}\n\n"
        f"Matches :\n{match_lines}\n\n"
        f"Answer :\n{result.answer}\n\n"
        f"Gaps :\n{gap_lines}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Founder OS local knowledge-base search")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument(
        "--dirs",
        nargs="+",
        default=DEFAULT_DIRS,
        help="Directories to search relative to the repo root",
    )
    parser.add_argument("--limit", type=int, default=3, help="Maximum number of matches")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.query:
        query = args.query.strip()
    else:
        query = sys.stdin.read().strip()

    if not query:
        print("No query provided.", file=sys.stderr)
        return 1

    result = search(query, args.dirs, args.limit)

    if args.json:
        print(
            json.dumps(
                {
                    "query": result.query,
                    "matches": [
                        {
                            "source_path": match.source_path,
                            "excerpt": match.excerpt,
                            "confidence": match.confidence,
                        }
                        for match in result.matches
                    ],
                    "answer": result.answer,
                    "gaps": result.gaps,
                },
                ensure_ascii=True,
                indent=2,
            )
        )
    else:
        print(to_text(result))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
