# Day 2 Coach Memory

## Date du run

`2026-07-17`

## Stack utilisee

- mode : local
- stockage memoire : `vault/` en markdown
- agent : `scripts/coach_memory_agent.py`
- runtime : `Python 3`
- cloud : aucun

## Question posee

```text
A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?
```

## Commande executee

```bash
python3 scripts/coach_memory_agent.py --json "A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?"
```

## Notes ou sources utilisees

- `70-learning/learning-backlog.md`
- `20-clients/client-pains-and-objections.md`
- `20-clients/ideal-client-profile.md`
- `30-offers/core-offer.md`
- `10-business/business-brief.md`

## Reponse obtenue

```json
{
  "question": "A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?",
  "answer": "Priorite de la semaine :\n1. discovery and qualification calls\n2. objection handling for small B2B sales\n3. local SEO fundamentals\n\nPourquoi :\n- ces apprentissages reduisent le risque de vendre une offre mal cadree\n- ils aident a mieux qualifier les prospects et a repondre aux objections\n- ils soutiennent directement le lancement commercial a court terme\n\nNotes utilisees : 70-learning/learning-backlog.md, 20-clients/client-pains-and-objections.md, 20-clients/ideal-client-profile.md",
  "sources": [
    {
      "path": "70-learning/learning-backlog.md",
      "score": 14,
      "snippets": [
        "## Current Gaps",
        "## This Week Candidates",
        "## Coach Signals"
      ]
    },
    {
      "path": "20-clients/client-pains-and-objections.md",
      "score": 7,
      "snippets": [
        "## Coach Signals"
      ]
    },
    {
      "path": "20-clients/ideal-client-profile.md",
      "score": 7,
      "snippets": [
        "## Coach Signals",
        "## Coach Signals"
      ]
    },
    {
      "path": "30-offers/core-offer.md",
      "score": 7,
      "snippets": [
        "## Coach Signals"
      ]
    },
    {
      "path": "10-business/business-brief.md",
      "score": 6,
      "snippets": [
        "## Coach Signals"
      ]
    }
  ],
  "limits": [
    "Le classement est lexical, pas semantique.",
    "L'agent repond uniquement a partir des notes locales du vault.",
    "La priorisation reste un support de decision, pas une verite business prouvee."
  ]
}
```

## Analyse des limites

- le resultat depend de la qualite redactionnelle des notes
- il n'y a pas de recherche semantique ni de reranking
- les citations sont fiables sur les fichiers et sur des extraits courts, mais pas encore sur des lignes exactes
- l'agent priorise bien le lancement d'offre, mais il ne mesure pas l'impact reel sur des ventes observees

## Donnees envoyees au cloud si applicable

Aucune. Tout le traitement est local.
