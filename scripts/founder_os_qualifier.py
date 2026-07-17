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
    lead_name: str
    source: str
    summary: str
    pain_level: str
    fit_score: int
    estimated_scope: str
    risks: list[str]
    missing_information: list[str]
    recommended_agents: list[str]
    human_validation_required: bool
    next_action: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def dedupe(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


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

    return dedupe(agents)


def detect_risks(request: str) -> list[str]:
    text = normalize(request)
    risks: list[str] = []

    if any(keyword in text for keyword in ["prix", "budget", "devis", "tarif", "delai"]):
        risks.append(
            "Annoncer un prix ou un delai trop tot sans avoir cadre le nombre de pages, "
            "les contenus disponibles, les besoins SEO et les fonctionnalites attendues."
        )

    if any(keyword in text for keyword in ["site", "vitrine", "refonte", "seo"]):
        risks.append(
            "Mal qualifier le perimetre de la demande et lancer un cadrage trop vague, ce qui "
            "cree ensuite du scope creep et des promesses floues."
        )

    if not risks:
        risks.append(
            "Informations insuffisantes pour evaluer le besoin sans risque d'extrapolation."
        )

    return risks


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


def detect_pain_level(request: str) -> str:
    text = normalize(request)

    if any(keyword in text for keyword in ["urgent", "delai", "rapidement", "vite"]):
        return "high"
    if any(keyword in text for keyword in ["prix", "budget", "devis", "site", "seo"]):
        return "medium"
    return "low"


def estimate_scope(request: str) -> str:
    text = normalize(request)

    if "site vitrine" in text:
        return "site vitrine MVP"
    if "seo" in text or "referencement" in text:
        return "audit SEO initial"
    return "a qualifier"


def detect_missing_information(request: str) -> list[str]:
    text = normalize(request)
    missing: list[str] = []

    if not any(keyword in text for keyword in ["page", "pages"]):
        missing.append("nombre_de_pages")
    if "contenu" not in text and "textes" not in text:
        missing.append("contenus_disponibles")
    if "zone geographique" not in text and "local" not in text and "ville" not in text:
        missing.append("zone_geographique_cible")
    if "delai" not in text and "urgent" not in text:
        missing.append("niveau_urgence")
    if "budget" not in text and "prix" not in text and "devis" not in text:
        missing.append("budget_indicatif")

    return missing


def requires_human_validation(request: str) -> bool:
    text = normalize(request)
    return any(keyword in text for keyword in ["prix", "budget", "devis", "tarif", "delai"])


def detect_fit_score(request: str) -> int:
    text = normalize(request)
    score = 40

    if any(keyword in text for keyword in ["site", "vitrine", "seo", "google"]):
        score += 20
    if any(keyword in text for keyword in ["artisan", "commerce", "prestations"]):
        score += 15
    if any(keyword in text for keyword in ["prix", "devis", "budget"]):
        score += 10
    if len(detect_missing_information(request)) <= 2:
        score += 10

    return min(score, 95)


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
        lead_name="A verifier",
        source="inbound_request",
        summary=build_reformulation(request),
        pain_level=detect_pain_level(request),
        fit_score=detect_fit_score(request),
        estimated_scope=estimate_scope(request),
        risks=detect_risks(request),
        missing_information=detect_missing_information(request),
        recommended_agents=detect_agents(request),
        human_validation_required=requires_human_validation(request),
        next_action=next_action(request),
    )


def to_text(result: Qualification) -> str:
    agent_lines = "\n".join(f"- {agent}" for agent in result.recommended_agents)
    risk_lines = "\n".join(f"- {risk}" for risk in result.risks)
    missing_lines = "\n".join(f"- {item}" for item in result.missing_information) or "- aucune"
    validation = "Oui" if result.human_validation_required else "Non"

    return (
        f"Lead name :\n{result.lead_name}\n\n"
        f"Source :\n{result.source}\n\n"
        f"Besoin reformule :\n{result.summary}\n\n"
        f"Pain level :\n{result.pain_level}\n\n"
        f"Fit score :\n{result.fit_score}\n\n"
        f"Estimated scope :\n{result.estimated_scope}\n\n"
        f"Risques :\n{risk_lines}\n\n"
        f"Informations manquantes :\n{missing_lines}\n\n"
        f"Agents a mobiliser :\n{agent_lines}\n\n"
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
                    "lead_name": result.lead_name,
                    "source": result.source,
                    "summary": result.summary,
                    "pain_level": result.pain_level,
                    "fit_score": result.fit_score,
                    "estimated_scope": result.estimated_scope,
                    "risks": result.risks,
                    "missing_information": result.missing_information,
                    "recommended_agents": result.recommended_agents,
                    "human_validation_required": result.human_validation_required,
                    "next_action": result.next_action,
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
