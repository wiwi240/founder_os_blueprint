# Day 1 First Agent Local

## Date du run

`2026-07-16`

## Environnement

- mode : local
- runtime : `Python 3`
- dependances : aucune dependance externe
- type d'agent : moteur de qualification deterministe a base de regles

## Commande executee

```bash
python3 scripts/founder_os_qualifier.py "Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir."
```

## Sortie obtenue

```text
Besoin reformule :
Le prospect veut un site vitrine simple pour presenter ses prestations de renovation, rassurer ses futurs clients et generer des prises de contact. Il attend une premiere estimation de prix, un delai probable et la liste des elements a fournir pour lancer le projet.

Agents a mobiliser :
- Agent Code / Produit
- Agent Mail / Sales
- Agent Admin / Compta
- Agent SEO

Risque principal :
Annoncer un prix ou un delai trop tot sans avoir cadre le nombre de pages, les contenus disponibles, les besoins SEO et les fonctionnalites attendues.

Validation humaine requise :
Oui

Prochaine action :
Envoyer un mini questionnaire de cadrage ou planifier un appel de 15 a 20 minutes pour confirmer le nombre de pages, les contenus disponibles, la zone geographique cible, les references visuelles et le niveau d'urgence avant de preparer une estimation.
```

## Analyse qualite

- point fort : run local reel, sans dependance cloud
- point fort : sortie stable et reproductible
- limite : reformulation moins souple qu'un LLM
- limite : couverture limitee a des heuristiques explicites

## Analyse cout

- cout logiciel : nul
- cout execution : negligeable
- cout maintenance : faible tant que le nombre de regles reste petit

## Donnees exposees

- aucune donnee envoyee a un fournisseur externe
- les donnees restent locales sur la machine

## Prochaine amelioration

- ajouter une section `informations manquantes`
- externaliser les regles dans un fichier de config
- ajouter des tests automatiques pour plusieurs types de demandes
