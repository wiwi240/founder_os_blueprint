# Day 2 Tool Catalog Local

## Date du run

`2026-07-17`

## Environnement

- mode : local
- runtime : `Python 3`
- dependances : aucune dependance externe
- type d'actions executees : qualification de lead et recherche documentaire

## Commande 1 executee

```bash
python3 scripts/founder_os_qualifier.py --json "Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir."
```

## Sortie 1 obtenue

```json
{
  "lead_name": "A verifier",
  "source": "inbound_request",
  "summary": "Le prospect veut un site vitrine simple pour presenter ses prestations de renovation, rassurer ses futurs clients et generer des prises de contact. Il attend une premiere estimation de prix, un delai probable et la liste des elements a fournir pour lancer le projet.",
  "pain_level": "high",
  "fit_score": 85,
  "estimated_scope": "site vitrine MVP",
  "risks": [
    "Annoncer un prix ou un delai trop tot sans avoir cadre le nombre de pages, les contenus disponibles, les besoins SEO et les fonctionnalites attendues.",
    "Mal qualifier le perimetre de la demande et lancer un cadrage trop vague, ce qui cree ensuite du scope creep et des promesses floues."
  ],
  "missing_information": [
    "nombre_de_pages",
    "contenus_disponibles",
    "zone_geographique_cible"
  ],
  "recommended_agents": [
    "Agent Code / Produit",
    "Agent Mail / Sales",
    "Agent Admin / Compta",
    "Agent SEO"
  ],
  "human_validation_required": true,
  "next_action": "Envoyer un mini questionnaire de cadrage ou planifier un appel de 15 a 20 minutes pour confirmer le nombre de pages, les contenus disponibles, la zone geographique cible, les references visuelles et le niveau d'urgence avant de preparer une estimation."
}
```

## Commande 2 executee

```bash
python3 scripts/search_knowledge_base.py --json "quelles actions demandent une validation humaine dans la policy"
```

## Sortie 2 obtenue

```json
{
  "query": "quelles actions demandent une validation humaine dans la policy",
  "matches": [
    {
      "source_path": "docs/permissions-policy.md",
      "excerpt": "# Permissions Policy",
      "confidence": "high"
    },
    {
      "source_path": "docs/structured-outputs.md",
      "excerpt": "Si un agent ne peut pas remplir un champ sans extrapoler, il doit laisser une valeur vide exploitable ou expliciter `A verifier`. Inventer pour \"completer le JSON\" est une faute de conception.",
      "confidence": "high"
    },
    {
      "source_path": "docs/run-journal.md",
      "excerpt": "- Quelles preuves minimales doit-on conserver pour auditer une action agentique ?",
      "confidence": "high"
    }
  ],
  "answer": "3 source(s) trouvee(s) pour la requete. La meilleure source est docs/permissions-policy.md.",
  "gaps": []
}
```

## Analyse

- point fort : deux actions locales reelles sont maintenant executables
- point fort : le qualifier sort un schema structure coherent avec la documentation
- limite : le moteur de recherche classe les sources simplement ; ce n'est pas un vrai moteur semantique
- limite : les extraits restent bruts et ne ciblent pas encore toujours la ligne la plus utile
