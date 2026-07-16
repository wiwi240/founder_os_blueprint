#!/usr/bin/env python3
"""Minimal local agent to qualify inbound requests for Web Studio OS."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Qualification:
    reformulation: str
    agents: list[str]
    risk: str
    human_validation_required: bool
    next_action: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def detect_agents(request: str) -> list[str]:
    text = normalize(request)
    agents = ["Agent Code / Produit", "Agent Mail / Sales"]

    if any(keyword in text for keyword in ["prix", "budget", "devis", "tarif"]):
        agents.append("Agent Admin / Compta")

    if any(
        keyword in text
        for keyword in [
            "site",
            "vitrine",
            "seo",
            "referencement",
            "google",
            "prestations",
        ]
    ):
        agents.append("Agent SEO")

    return agents


def detect_risk(request: str) -> str:
    text = normalize(request)

    if any(keyword in text for keyword in ["prix", "budget", "devis", "tarif", "delai"]):
        return (
            "Annoncer un prix ou un delai trop tot sans avoir cadre le nombre de pages, "
            "les contenus disponibles, les besoins SEO et les fonctionnalités attendues."
        )

    return (
        "Mal qualifier le perimetre de la demande et lancer un cadrage trop vague, ce qui "
        "cree ensuite du scope creep et des promesses floues."
    )


def build_reformulation(request: str) -> str:
    text = normalize(request)

    if "artisan" in text and "renovation" in text and "site vitrine" in text:
        return (
            "Le prospect veut un site vitrine simple pour presenter ses prestations de "
            "renovation, rassurer ses futurs clients et generer des prises de contact. "
            "Il attend une premiere estimation de prix, un delai probable et la liste des "
            "elements a fournir pour lancer le projet."
        )

    return (
        "Le prospect exprime un besoin commercial ou digital qui doit etre recadre en "
        "objectif concret, perimetre MVP, informations manquantes et conditions "
        "d'estimation avant toute promesse."
    )


def requires_human_validation(request: str) -> bool:
    text = normalize(request)
    return any(keyword in text for keyword in ["prix", "budget", "devis", "tarif", "delai"])


def next_action(request: str) -> str:
    text = normalize(request)

    if any(keyword in text for keyword in ["prix", "budget", "devis", "tarif", "delai"]):
        return (
            "Envoyer un mini questionnaire de cadrage ou planifier un appel de 15 a 20 "
            "minutes pour confirmer le nombre de pages, les contenus disponibles, la zone "
            "geographique cible, les references visuelles et le niveau d'urgence avant de "
            "preparer une estimation."
        )

    return (
        "Collecter les informations manquantes sur le besoin, le contexte et la priorite "
        "business avant de router vers les agents suivants."
    )


def qualify(request: str) -> Qualification:
    return Qualification(
        reformulation=build_reformulation(request),
        agents=detect_agents(request),
        risk=detect_risk(request),
        human_validation_required=requires_human_validation(request),
        next_action=next_action(request),
    )


def to_text(result: Qualification) -> str:
    agent_lines = "\n".join(f"- {agent}" for agent in result.agents)
    validation = "Oui" if result.human_validation_required else "Non"

    return (
        f"Besoin reformule :\n{result.reformulation}\n\n"
        f"Agents a mobiliser :\n{agent_lines}\n\n"
        f"Risque principal :\n{result.risk}\n\n"
        f"Validation humaine requise :\n{validation}\n\n"
        f"Prochaine action :\n{result.next_action}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Founder OS local lightweight qualifier")
    parser.add_argument("request", nargs="?", help="Inbound request to qualify")
    parser.add_argument("--input-file", help="Read the request from a text file")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.input_file:
        with open(args.input_file, "r", encoding="utf-8") as handle:
            request = handle.read().strip()
    elif args.request:
        request = args.request.strip()
    else:
        request = sys.stdin.read().strip()

    if not request:
        print("No request provided.", file=sys.stderr)
        return 1

    result = qualify(request)

    if args.json:
        print(
            json.dumps(
                {
                    "besoin_reformule": result.reformulation,
                    "agents_a_mobiliser": result.agents,
                    "risque_principal": result.risk,
                    "validation_humaine_requise": result.human_validation_required,
                    "prochaine_action": result.next_action,
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
