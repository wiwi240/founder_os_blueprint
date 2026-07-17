# Tool Tests

## Cadre

- date : `2026-07-17`
- environnement : `local`
- principe : melanger tests reels et actions simulees documentees
- limite : deux actions sont reellement implementees a ce stade dans le repo ; le reste sert a valider le design des interfaces et des garde-fous

## Test 1 : `qualify_lead`

### Input

```text
Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir.
```

### Sortie attendue

- besoin reformule
- agents a mobiliser
- risque principal
- validation humaine requise
- prochaine action

### Sortie obtenue

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

### Verdict

`OK`

### Correction a faire

- renseigner `lead_name` des que la source fournit un nom exploitable

## Test 2 : `search_knowledge_base`

### Input

```text
Question : quelles actions demandent une validation humaine dans la policy ?
Dossier cible : docs/
```

### Sortie attendue

- liste de sources
- extrait traceable
- reponse courte

### Sortie obtenue

```json
{
  "query": "quelles actions demandent une validation humaine dans la policy ?",
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

### Verdict

`OK`

### Correction a faire

- ameliorer encore l'extrait pour viser directement les lignes du tableau de policy

## Test 3 : `draft_email_reply`

### Input

```json
{
  "lead_name": "Atelier Rive Gauche",
  "context": "Le prospect demande s'il est possible d'avoir un devis rapide pour un site vitrine de 5 pages.",
  "goal": "proposer un cadrage court avant estimation",
  "tone": "professional"
}
```

### Sortie attendue

- objet
- corps du mail
- CTA
- statut brouillon

### Sortie obtenue

```json
{
  "subject": "Re: estimation pour votre site vitrine",
  "recipient_context": "Prospect inbound demandant un devis rapide pour un site vitrine 5 pages",
  "tone": "professional",
  "goal": "obtenir les informations minimales avant estimation",
  "body_markdown": "Bonjour,\n\nMerci pour votre message. Je peux preparer une estimation de travail, mais j'ai besoin de confirmer quelques points d'abord : nombre de pages exact, contenus deja disponibles, objectifs commerciaux et delai souhaite.\n\nSi vous voulez, je vous envoie un mini questionnaire ou nous prenons un appel de 15 minutes.\n\nBien a vous,",
  "cta": "Choisir entre questionnaire ou appel court",
  "approval_status": "draft_only",
  "warnings": [
    "Ne pas envoyer sans validation humaine",
    "Ne pas annoncer de prix ferme dans ce brouillon"
  ]
}
```

### Verdict

`OK`

### Correction a faire

- prevoir une variante plus courte pour les leads froids

## Test 4 : `create_mock_quote`

### Input

```json
{
  "client_name": "Atelier Rive Gauche",
  "scope": "site vitrine 5 pages",
  "options": ["blog", "seo local"],
  "currency": "EUR"
}
```

### Sortie attendue

- lignes de devis
- total indicatif
- hypothese
- mention non contractuelle

### Sortie obtenue

```json
{
  "quote_id": "MOCK-2026-07-17-001",
  "client_name": "Atelier Rive Gauche",
  "currency": "EUR",
  "items": [
    {
      "label": "Cadrage et arborescence",
      "quantity": 1,
      "unit_price": 250,
      "line_total": 250
    },
    {
      "label": "Design et integration site vitrine 5 pages",
      "quantity": 1,
      "unit_price": 1450,
      "line_total": 1450
    }
  ],
  "subtotal": 1700,
  "options": [
    {
      "label": "Blog",
      "price": 300
    },
    {
      "label": "SEO local initial",
      "price": 250
    }
  ],
  "total_estimate": 2250,
  "assumptions": [
    "Contenus textes fournis par le client",
    "Pas d'espace membre ni de paiement en ligne"
  ],
  "disclaimer": "Devis fictif sans valeur contractuelle",
  "human_validation_required": true
}
```

### Verdict

`OK avec reserve`

### Correction a faire

- ajouter une date de validite fictive
- rendre visible que les options ne sont pas incluses dans le `subtotal`

## Test 5 : bonus `n8n draft_email_reply`

### Input

```json
{
  "lead_name": "Atelier Rive Gauche",
  "context": "Le prospect demande s'il est possible d'avoir un devis rapide pour un site vitrine de 5 pages.",
  "goal": "proposer un cadrage court avant estimation",
  "tone": "professional"
}
```

### Sortie attendue

- workflow importable dans `n8n`
- sortie JSON de brouillon de mail
- aucun envoi reel

### Sortie obtenue

```text
Fichier cree : automations/n8n/draft-email-reply-workflow.json
Type : workflow n8n importable
Noeuds : Manual Trigger -> Sample Input -> Compose Draft
Mode : draft_only
```

### Verdict

`OK`

### Correction a faire

- remplacer le `Sample Input` par un vrai `Webhook` ou `Form Trigger` dans une instance n8n reelle
- remplacer la composition template par un noeud LLM seulement si les risques de cout et d'exposition de donnees sont acceptes

## Conclusion

Le systeme est plus credible qu'avant : `qualify_lead` et `search_knowledge_base` existent reellement en script local, et `draft_email_reply` dispose maintenant d'un premier workflow `n8n` importable. En revanche, `create_mock_quote`, `extract_seo_keywords`, `write_note_draft` et `summarize_call_notes` restent des contrats d'interface. Le repo est donc partiellement actionnable, avec un bonus no-code reellement versionne.
