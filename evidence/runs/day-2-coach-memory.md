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
      "score": 13.0,
      "snippets": [
        {
          "line_number": 13,
          "text": "- write a sharper qualification checklist"
        },
        {
          "line_number": 14,
          "text": "- create a one-page offer framing"
        },
        {
          "line_number": 15,
          "text": "- practice three sales reply templates"
        },
        {
          "line_number": 16,
          "text": "- define the minimum SEO audit checklist"
        }
      ]
    },
    {
      "path": "20-clients/client-pains-and-objections.md",
      "score": 9.0,
      "snippets": [
        {
          "line_number": 19,
          "text": "- learn objection handling for price and scope"
        },
        {
          "line_number": 20,
          "text": "- learn to explain deliverables in plain language"
        },
        {
          "line_number": 21,
          "text": "- learn to tie each feature to a concrete business outcome"
        }
      ]
    },
    {
      "path": "20-clients/ideal-client-profile.md",
      "score": 9.0,
      "snippets": [
        {
          "line_number": 18,
          "text": "- learn how to qualify fit fast"
        },
        {
          "line_number": 19,
          "text": "- learn how to frame an MVP in business language"
        },
        {
          "line_number": 20,
          "text": "- learn the few questions that expose scope risk early"
        }
      ]
    },
    {
      "path": "30-offers/core-offer.md",
      "score": 9.0,
      "snippets": [
        {
          "line_number": 22,
          "text": "- learn how to productize the offer"
        },
        {
          "line_number": 23,
          "text": "- learn how to define a clean scope boundary"
        },
        {
          "line_number": 24,
          "text": "- learn how to present options without creating confusion"
        }
      ]
    },
    {
      "path": "10-business/business-brief.md",
      "score": 8.0,
      "snippets": [
        {
          "line_number": 19,
          "text": "- learning should support revenue in the next 30 days"
        },
        {
          "line_number": 13,
          "text": "- sell clear MVP website offers first"
        },
        {
          "line_number": 14,
          "text": "- avoid custom builds with vague scope"
        }
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
- le retrieval reste lexical, meme s'il tient mieux compte des sections utiles
- il n'y a pas de recherche semantique a embeddings ni de reranking externe
- les citations donnent maintenant des extraits avec numeros de ligne, mais pas une granularite de paragraphe ou de chunk versionne
- l'agent priorise bien le lancement d'offre, mais il ne mesure pas l'impact reel sur des ventes observees

## Donnees envoyees au cloud si applicable

Aucune. Tout le traitement est local.
