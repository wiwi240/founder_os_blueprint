# Provider Choice

## Choix retenu pour l'exercice

Je retiens `OpenAI` en cloud pour le premier agent `Founder OS Qualifier`.

Ce choix n'est pas ideologique. Il est simplement plus propre pour un day 1 que de simuler une architecture locale fragile sans vraie preuve de qualite.

## Probleme reel a resoudre

Le vrai besoin n'est pas "avoir un agent".

Le vrai besoin est de qualifier vite une demande entrante sans :

- promettre n'importe quoi
- sous-estimer le scope
- envoyer des informations sensibles sans cadre

Pour ce besoin, la priorite est la qualite de raisonnement et la vitesse d'execution, pas l'optimisation d'infrastructure.

## Pourquoi OpenAI

- bon niveau de reformulation et de synthese pour un agent de qualification
- setup minimal pour produire une preuve rapidement
- compatible avec une approche simple : prompt systeme + entree utilisateur + sortie structuree

## Pourquoi je n'ai pas choisi un setup local pour ce run

Un setup local aurait ajoute plusieurs inconnues des le day 1 :

- qualite variable selon la machine et le modele
- temps de setup plus long que la valeur de l'exercice
- risque de confondre evaluation de l'agent et evaluation de l'infrastructure

Pour un premier exercice, c'est une mauvaise priorite.

## Donnees envoyees au cloud

Dans ce flux, les donnees potentiellement envoyees sont :

- le texte du besoin prospect
- quelques metadonnees commerciales
- les hypotheses de budget, delai ou contenus

Donnees a exclure par defaut :

- secrets
- acces clients
- contrats complets
- pieces administratives non necessaires
- donnees sensibles sans besoin operationnel clair

## Cout potentiel

Le cout est faible pour un run manuel de qualification.

Il devient significatif uniquement si :

- le volume de demandes augmente fortement
- on ajoute plusieurs passes de raisonnement
- on orchestre plusieurs agents sur chaque lead

Conclusion pratique :

- day 1 : cout acceptable
- a partir d'un vrai volume : suivre le cout par run et definir un budget mensuel

Je n'indique pas de chiffre exact ici car ce serait fragile sans verrouiller le modele et la grille tarifaire du moment. A verifier avant usage recurrent.

## Limites du choix cloud

- dependance fournisseur
- surface d'exposition des donnees plus large qu'en local
- cout variable
- necessite d'une politique claire sur ce qui peut etre envoye

## Decision MVP

Le choix rationnel pour cet exercice est :

- memoire et documentation dans le repo local
- qualification textuelle via OpenAI cloud

Si demain le besoin evolue vers de gros volumes ou des donnees plus sensibles, il faudra reevaluer un mode hybride ou local. Pas avant.
