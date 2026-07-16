# Founder OS Blueprint

Ce repository pose les fondations d'un `Founder OS` pour une micro-agence de developpement web assistee par IA.

Le projet retenu pour ce blueprint est `Web Studio OS` : un systeme multi-agents concu pour aider un founder a gerer la prospection, le cadrage, la production, le suivi commercial et une partie de l'operationnel.

## Objectif

Le but n'est pas de construire toute la plateforme des le premier jour.

Le but est de definir clairement :

- le contexte business
- l'architecture cible
- les roles des agents
- les permissions et actions sensibles
- la strategie local/cloud
- les preuves attendues lors des executions

## Contenu du repo

- `docs/business-brief.md` : brief business du projet
- `docs/architecture.md` : architecture cible et schema Mermaid
- `docs/agent-roles.md` : definition detaillee des agents
- `docs/permissions-policy.md` : politique de permissions et actions sensibles
- `docs/provider-choice.md` : choix provisoire entre local, cloud ou hybride
- `docs/run-journal.md` : journal de travail du jour 1
- `evidence/screenshots/` : captures et preuves visuelles
- `evidence/runs/` : traces d'execution et journaux de runs
- `exports/` : livrables exportes ou documents intermediaires
- `vault/` : memoire locale type Obsidian

## Agents couverts

Le blueprint couvre au minimum les agents suivants :

- Code / Produit
- SEO
- Prospection
- Mail / Sales
- Admin / Compta
- Coach

## Statut

Etat actuel : `day 1 blueprint`

- structure du repo creee
- documentation principale redigee
- branche de travail creee
- PR ouverte pour revue

Ce repo ne contient pas encore d'automatisation metier, de scripts d'orchestration ni d'integrations externes reelles.

## Logique MVP

Le choix est volontairement sobre.

Construire des agents sans cadre clair cree vite de la confusion, de la dette et des risques de permissions. Ce repository sert donc d'abord a verrouiller les fondations avant de passer a l'execution.

## Suite logique

Les prochaines etapes pertinentes seraient :

1. definir le format exact des fiches dans `vault/`
2. choisir un orchestrateur minimal
3. formaliser les entrees/sorties en templates
4. tester un premier flux simple de qualification prospect vers brouillon email
