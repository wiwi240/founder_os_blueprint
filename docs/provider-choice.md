# Provider Choice

## Choix provisoire

Je choisis un mode hybride :

- vault et documentation en local
- modeles et services d'automatisation en cloud

## Raisonnement

### Pourquoi pas full local

Le full local est seduisant pour la confidentialite et le cout marginal, mais il est souvent plus fragile pour un MVP : qualite des modeles variable, maintenance machine, temps de setup, et limites si la machine n'est pas dimensionnee.

### Pourquoi pas full cloud

Le full cloud simplifie la qualite et l'integration, mais il augmente les couts, la dependance fournisseur et les risques de diffusion excessive d'informations si la gouvernance est faible.

### Pourquoi hybride

Le besoin principal day 1 est de separer :

- la memoire durable, qui reste locale
- la capacite de raisonnement/generation, qui peut etre deleguee a des modeles cloud

## Decision pratique

- Obsidian / `vault/` en local pour la memoire projet
- LLM cloud pour la redaction, l'analyse, les brouillons et l'orchestration initiale
- Re-evaluation plus tard si le volume ou la confidentialite justifient du local avec Ollama ou equivalent

## Compromis assumes

- Avantage : mise en route rapide
- Avantage : memoire metier sous controle local
- Risque : cout variable des appels cloud
- Risque : discipline necessaire sur ce qui peut sortir vers un fournisseur externe
