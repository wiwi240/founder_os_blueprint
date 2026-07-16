# First Agent Config

## Nom de l'agent

`Founder OS Qualifier`

## Plateforme utilisee

- Fournisseur : local
- Mode : CLI locale
- Runtime : `Python 3`
- Dependances : aucune
- Type d'usage : une commande locale qui prend une demande texte et retourne une sortie structuree

## Pourquoi ce choix

Je retiens un agent local deterministe pour quatre raisons :

- execution reelle depuis le repo
- zero cout API
- zero exposition cloud des donnees
- setup extremement leger et defendable pour un MVP

Ce n'est pas une architecture finale. C'est un choix MVP pour prouver le fonctionnement d'un agent local avant d'ajouter un LLM ou une orchestration plus riche.

## Instructions

Logique de l'agent :

```text
Role :
- qualifier une demande entrante pour Web Studio OS
- reformuler le besoin
- identifier les agents Founder OS a mobiliser
- signaler le risque principal
- dire si une validation humaine est necessaire
- proposer la prochaine action

Regles :
- ne jamais promettre un prix ou un delai ferme
- exiger une validation humaine si la demande mentionne prix, devis, budget ou delai
- rester sur un scope MVP
- appliquer des heuristiques explicites et lisibles
```

## Format de sortie attendu

```text
Besoin reformule :
...

Agents a mobiliser :
- ...

Risque principal :
...

Validation humaine requise :
Oui / Non

Prochaine action :
...
```

## Limites de l'agent

- il ne comprend pas le langage naturel aussi finement qu'un LLM
- il ne chiffre pas de devis fiable sans hypotheses explicites
- il ne donne pas de delai ferme sans validation humaine
- il ne verifie pas seul la solvabilite, le secteur ou les contraintes legales du prospect
- il n'extrait pas automatiquement les pieces manquantes si elles ne sont pas fournies
- il ne remplace pas un call de cadrage quand le besoin est flou

## Conditions de validation humaine

Validation humaine requise si la sortie contient :

- une estimation de prix
- un delai annonce au prospect
- un engagement de scope
- une recommandation commerciale externe prete a etre envoyee
