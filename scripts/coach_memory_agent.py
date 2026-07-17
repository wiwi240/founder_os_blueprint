#!/usr/bin/env python3
"""Local Coach agent that answers from the Founder OS vault and cites note sources."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault"
TEXT_EXTENSIONS = {".md", ".txt"}
STOPWORDS = {
    "a",
    "alors",
    "au",
    "aux",
    "avec",
    "ce",
    "ces",
    "cette",
    "dans",
    "de",
    "des",
    "dois",
    "doit",
    "elle",
    "en",
    "et",
    "il",
    "je",
    "la",
    "le",
    "les",
    "ma",
    "mes",
    "mes",
    "mieux",
    "mon",
    "nos",
    "notes",
    "offre",
    "pour",
    "que",
    "quoi",
    "re",
    "se",
    "semaines",
    "semaine",
    "son",
    "sur",
    "ta",
    "tes",
    "this",
    "to",
    "ton",
    "un",
    "une",
    "utiliser",
    "we",
}

FOLDER_WEIGHTS = {
    "70-learning": 4,
    "30-offers": 3,
    "20-clients": 3,
    "50-sales-mail": 2,
    "40-seo-market": 2,
    "10-business": 2,
    "60-admin": 1,
    "90-agent-runs": 1,
}


@dataclass(frozen=True)
class NoteMatch:
    path: str
    score: int
    snippets: list[str]


@dataclass(frozen=True)
class CoachResponse:
    question: str
    answer: str
    sources: list[NoteMatch]
    limits: list[str]


def normalize(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if token not in STOPWORDS and len(token) > 1
    ]


def iter_notes() -> list[Path]:
    notes: list[Path] = []
    for path in VAULT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            notes.append(path)
    return sorted(notes)


def note_score(path: Path, text: str, keywords: list[str]) -> tuple[int, list[str]]:
    lowered = text.lower()
    score = FOLDER_WEIGHTS.get(path.parts[-2], 0)
    snippets: list[str] = []

    for keyword in keywords:
        if keyword in lowered:
            score += 2

    for line in text.splitlines():
        stripped = line.strip()
        lowered_line = stripped.lower()
        if not stripped:
            continue
        if any(keyword in lowered_line for keyword in keywords):
            snippets.append(stripped)
            score += 1
        if "coach signals" in lowered_line:
            score += 2
            snippets.append(stripped)
        if "this week candidates" in lowered_line or "current gaps" in lowered_line:
            snippets.append(stripped)

    if "this week candidates" in lowered:
        score += 4
    if "current gaps" in lowered:
        score += 2
    if "learn" in lowered:
        score += 2

    if not snippets:
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                snippets.append(stripped)
            if len(snippets) >= 3:
                break

    return score, snippets[:4]


def collect_learning_actions(sources: list[NoteMatch]) -> list[str]:
    actions: list[str] = []

    for source in sources:
        note_path = VAULT / source.path
        text = note_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            stripped = line.strip()
            lowered = stripped.lower()
            if stripped.startswith("- ") and any(
                marker in lowered
                for marker in [
                    "learn",
                    "write",
                    "create",
                    "practice",
                    "define",
                    "qualify",
                    "discovery",
                    "objection",
                    "seo",
                    "scope",
                    "offer",
                ]
            ):
                actions.append(stripped[2:])

    deduped: list[str] = []
    seen: set[str] = set()
    for action in actions:
        key = action.lower()
        if key not in seen:
            deduped.append(action)
            seen.add(key)

    return deduped[:6]


def answer_question(question: str, limit: int = 5) -> CoachResponse:
    keywords = normalize(question)
    matches: list[NoteMatch] = []

    for path in iter_notes():
        rel_path = str(path.relative_to(VAULT))
        text = path.read_text(encoding="utf-8")
        score, snippets = note_score(path, text, keywords)
        if score <= 0:
            continue
        matches.append(NoteMatch(path=rel_path, score=score, snippets=snippets))

    matches.sort(key=lambda item: (-item.score, item.path))
    sources = matches[:limit]

    if not sources:
        return CoachResponse(
            question=question,
            answer="Je ne sais pas. Aucune note exploitable n'a ete trouvee dans le vault.",
            sources=[],
            limits=["Le vault ne contient pas assez de notes pertinentes pour repondre."],
        )

    actions = collect_learning_actions(sources)
    if not actions:
        actions = [
            "clarifier l'offre et les criteres de qualification",
            "formaliser les objections frequentes et leurs reponses",
            "definir une checklist SEO locale minimale",
        ]

    top_actions = actions[:3]
    cited_paths = ", ".join(source.path for source in sources[:3])
    answer_lines = [
        "Priorite de la semaine :",
        f"1. {top_actions[0]}",
    ]
    if len(top_actions) > 1:
        answer_lines.append(f"2. {top_actions[1]}")
    if len(top_actions) > 2:
        answer_lines.append(f"3. {top_actions[2]}")

    answer_lines.extend(
        [
            "",
            "Pourquoi :",
            "- ces apprentissages reduisent le risque de vendre une offre mal cadree",
            "- ils aident a mieux qualifier les prospects et a repondre aux objections",
            "- ils soutiennent directement le lancement commercial a court terme",
            "",
            f"Notes utilisees : {cited_paths}",
        ]
    )

    limits = [
        "Le classement est lexical, pas semantique.",
        "L'agent repond uniquement a partir des notes locales du vault.",
        "La priorisation reste un support de decision, pas une verite business prouvee.",
    ]

    return CoachResponse(
        question=question,
        answer="\n".join(answer_lines),
        sources=sources,
        limits=limits,
    )


def to_text(result: CoachResponse) -> str:
    if result.sources:
        source_blocks = []
        for source in result.sources:
            snippets = " | ".join(source.snippets) if source.snippets else "A verifier"
            source_blocks.append(
                "\n".join(
                    [
                        f"- source: {source.path}",
                        f"  score: {source.score}",
                        f"  snippets: {snippets}",
                    ]
                )
            )
        sources_text = "\n".join(source_blocks)
    else:
        sources_text = "- aucune"

    limits_text = "\n".join(f"- {limit}" for limit in result.limits) or "- aucune"

    return (
        f"Question :\n{result.question}\n\n"
        f"Reponse :\n{result.answer}\n\n"
        f"Sources :\n{sources_text}\n\n"
        f"Limits :\n{limits_text}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Founder OS Coach agent using local vault notes")
    parser.add_argument("question", nargs="?", help="Question to answer from the vault")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of cited notes")
    args = parser.parse_args()

    if args.question:
        question = args.question.strip()
    else:
        question = sys.stdin.read().strip()

    if not question:
        print("No question provided.", file=sys.stderr)
        return 1

    result = answer_question(question, limit=args.limit)

    if args.json:
        print(
            json.dumps(
                {
                    "question": result.question,
                    "answer": result.answer,
                    "sources": [
                        {
                            "path": source.path,
                            "score": source.score,
                            "snippets": source.snippets,
                        }
                        for source in result.sources
                    ],
                    "limits": result.limits,
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
