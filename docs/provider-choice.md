# Provider Choice

## Choix retenu pour l'exercice

Je retiens un agent local leger en `Python 3` pour le premier agent `Founder OS Qualifier`.

Ce choix n'est pas ideologique. Il est simplement plus propre pour un day 1 que de documenter un agent cloud sans execution locale reelle depuis le repo.

## Probleme reel a resoudre

Le vrai besoin n'est pas "avoir un agent".

Le vrai besoin est de qualifier vite une demande entrante sans :

- promettre n'importe quoi
- sous-estimer le scope
- envoyer des informations sensibles sans cadre

Pour ce besoin, la priorite est d'avoir un agent qui tourne vraiment, qui soit lisible, testable et quasi gratuit a maintenir.

## Pourquoi un agent local deterministe

- execution locale immediate
- aucune dependance externe
- aucun cout variable
- comportement stable et reproductible
- bonne adequation avec un scope day 1 limite a la qualification

## Pourquoi je n'ai pas choisi un LLM local pour ce run

Un vrai LLM local aurait ajoute plusieurs inconnues des le day 1 :

- qualite variable selon la machine et le modele
- consommation machine inutile pour un besoin simple
- temps de setup plus long que la valeur pedagogique du livrable

Pour un premier exercice, c'est une mauvaise priorite.

## Donnees traitees

Dans ce flux, les donnees restent locales :

- le texte du besoin prospect
- quelques metadonnees commerciales
- les hypotheses de budget, delai ou contenus

Donnees a proteger malgre tout :

- secrets
- acces clients
- contrats complets
- pieces administratives non necessaires
- donnees sensibles sans besoin operationnel clair

## Cout potentiel

- cout logiciel : nul
- cout execution : negligeable
- cout maintenance : faible tant que l'agent reste simple

## Limites du choix local

- moins flexible qu'un LLM
- couverture fonctionnelle limitee aux regles implementees
- qualite de reformulation inferieure a un bon modele cloud
- necessite de faire evoluer les heuristiques a la main

## Decision MVP

Le choix rationnel pour cet exercice est :

- memoire, logique et preuves dans le repo local
- qualification textuelle via un agent CLI deterministe

Si demain le besoin evolue vers plus de cas ou des formulations plus floues, il faudra reevaluer un LLM local ou hybride. Pas avant.
