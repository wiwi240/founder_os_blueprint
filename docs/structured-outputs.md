# Structured Outputs

## Objectif

Les sorties structurees reduisent l'ambiguite, facilitent les tests et permettent un routage propre entre agents.

## Schema 1 : qualification de lead

```json
{
  "lead_name": "string",
  "source": "string",
  "summary": "string",
  "pain_level": "low | medium | high",
  "fit_score": 0,
  "estimated_scope": "string",
  "risks": ["string"],
  "missing_information": ["string"],
  "recommended_agents": ["string"],
  "human_validation_required": true,
  "next_action": "string"
}
```

## Schema 2 : brouillon de mail

```json
{
  "subject": "string",
  "recipient_context": "string",
  "tone": "professional | direct | warm",
  "goal": "string",
  "body_markdown": "string",
  "cta": "string",
  "approval_status": "draft_only",
  "warnings": ["string"]
}
```

## Schema 3 : devis fictif

```json
{
  "quote_id": "string",
  "client_name": "string",
  "currency": "EUR",
  "items": [
    {
      "label": "string",
      "quantity": 1,
      "unit_price": 0,
      "line_total": 0
    }
  ],
  "subtotal": 0,
  "options": [
    {
      "label": "string",
      "price": 0
    }
  ],
  "total_estimate": 0,
  "assumptions": ["string"],
  "disclaimer": "Devis fictif sans valeur contractuelle",
  "human_validation_required": true
}
```

## Schema 4 : recherche dans la memoire

```json
{
  "query": "string",
  "matches": [
    {
      "source_path": "string",
      "excerpt": "string",
      "confidence": "low | medium | high"
    }
  ],
  "answer": "string",
  "gaps": ["string"]
}
```

## Regles minimales

| Schema | Champs critiques | Motif |
| --- | --- | --- |
| Qualification de lead | `fit_score`, `risks`, `human_validation_required`, `next_action` | Evite les qualifications vagues et non actionnables |
| Brouillon de mail | `subject`, `body_markdown`, `approval_status` | Evite de confondre brouillon et envoi reel |
| Devis fictif | `items`, `total_estimate`, `disclaimer` | Rend visible le caractere non contractuel |
| Recherche memoire | `source_path`, `excerpt`, `confidence` | Force la tracabilite et limite l'invention |

## Point de vigilance

Si un agent ne peut pas remplir un champ sans extrapoler, il doit laisser une valeur vide exploitable ou expliciter `A verifier`. Inventer pour "completer le JSON" est une faute de conception.
