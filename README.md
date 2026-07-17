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
- `docs/memory-setup.md` : choix de la memoire locale et branchement du Coach
- `docs/coach-agent-config.md` : configuration du Coach local
- `docs/provider-choice.md` : choix provisoire entre local, cloud ou hybride
- `docs/run-journal.md` : journal de travail du jour 1
- `evidence/screenshots/` : captures et preuves visuelles
- `evidence/runs/` : traces d'execution et journaux de runs
- `exports/` : livrables exportes ou documents intermediaires
- `automations/n8n/` : bonus no-code versionne pour actions importables
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
- livrables day 1 prepares

Ce repo ne contient pas encore d'automatisation metier complete ni d'integrations externes reelles en production.
Il contient maintenant deux actions locales executables en CLI et un bonus `n8n` importable pour `draft_email_reply`.

## How To Run

Ce repo contient un agent local minimal executable en ligne de commande.

### Pre-requis

- `python3`
- ce repo clone localement

### Commandes

Run texte simple :

```bash
python3 scripts/founder_os_qualifier.py "Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir."
```

Run JSON :

```bash
python3 scripts/founder_os_qualifier.py --json "Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir."
```

Run depuis un fichier texte :

```bash
python3 scripts/founder_os_qualifier.py --input-file path/to/request.txt
```

Run via stdin :

```bash
echo "Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir." | python3 scripts/founder_os_qualifier.py
```

Recherche documentaire :

```bash
python3 scripts/search_knowledge_base.py --json "quelles actions demandent une validation humaine dans la policy"
```

Run Coach memoire :

```bash
python3 scripts/coach_memory_agent.py --json "A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?"
```

### Verification

La sortie doit contenir au minimum :

- besoin reformule
- agents a mobiliser
- risque principal
- validation humaine requise ou non
- prochaine action

### Reference

- configuration : [docs/first-agent-config.md](</home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/docs/first-agent-config.md>)
- configuration Coach : [docs/coach-agent-config.md](</home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/docs/coach-agent-config.md>)
- preuve locale de reference : [evidence/runs/day-1-first-agent-local.md](</home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/evidence/runs/day-1-first-agent-local.md>)
- preuve locale Coach : [evidence/runs/day-2-coach-memory.md](</home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/evidence/runs/day-2-coach-memory.md>)
- captures eventuelles : `evidence/screenshots/`

### Resultat attendu

Le run doit produire une qualification simple et prudente, sans promesse commerciale ferme sur le prix ou le delai sans validation humaine.

### Limites

- l'agent repose sur des regles simples, pas sur un raisonnement LLM
- aucune orchestration multi-agents complete n'est implementee
- la couverture des cas depend des heuristiques codees

## Bonus

Un workflow `n8n` importable est disponible pour l'action `draft_email_reply` :

- [automations/n8n/draft-email-reply-workflow.json](/home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/automations/n8n/draft-email-reply-workflow.json:1)
- [automations/n8n/README.md](/home/mon_pc/project/github/module%20thp/agent-builder/founder%20os/founder-_os_blueprint/automations/n8n/README.md:1)

## Logique MVP

Le choix est volontairement sobre.

Construire des agents sans cadre clair cree vite de la confusion, de la dette et des risques de permissions. Ce repository sert donc d'abord a verrouiller les fondations avant de passer a l'execution.

## Suite logique

Les prochaines etapes pertinentes seraient :

1. definir le format exact des fiches dans `vault/`
2. choisir un orchestrateur minimal
3. formaliser les entrees/sorties en templates
4. tester un premier flux simple de qualification prospect vers brouillon email
