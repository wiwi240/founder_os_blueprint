# n8n Bonus

## Objectif

Ce dossier contient un bonus day 2 : un workflow `n8n` versionne pour transformer l'action `draft_email_reply` en flux no-code importable.

## Workflow fourni

- `draft-email-reply-workflow.json`

## Ce que fait le workflow

1. recoit un payload d'entree depuis un formulaire ou un webhook ;
2. normalise les champs minimums du lead ;
3. construit un brouillon d'email commercial prudent ;
4. retourne une sortie JSON structuree au format `draft_email_reply`.

## Limites

- aucun envoi d'email reel ;
- aucune API payante ;
- workflow non execute dans ce repo faute d'instance `n8n` locale ;
- sortie deterministe basee sur templates, pas sur generation LLM.

## Import

Dans `n8n` :

1. ouvrir `Workflows`
2. choisir `Import from file`
3. selectionner `automations/n8n/draft-email-reply-workflow.json`

## Permissions

- mode brouillon uniquement
- validation humaine obligatoire avant tout envoi externe
