# Day 1 First Agent

## Date du run

`2026-07-16`

## Statut de preuve

Cette trace documente une sortie de reference produite dans cette session de travail Codex pour formaliser l'exercice.

Ce n'est pas la capture d'un run realise dans une interface externe dediee. Si l'evaluateur exige une preuve outillee stricte, il faudra refaire exactement ce test dans l'outil cible et ajouter la capture correspondante.

## Demande testee

> Un artisan me demande un site vitrine pour vendre ses prestations de renovation. Il veut savoir le prix, le delai et ce qu'il doit fournir.

## Sortie obtenue

```text
Besoin reformule :
Le prospect veut un site vitrine simple pour presenter ses prestations de renovation, rassurer ses futurs clients et generer des prises de contact. Il attend surtout une premiere estimation de prix, un delai probable et la liste des elements a fournir pour lancer le projet.

Agents a mobiliser :
- Agent Code / Produit
- Agent Mail / Sales
- Agent Admin / Compta
- Agent SEO

Risque principal :
Sous-estimer le perimetre du site et annoncer trop tot un prix ou un delai sans avoir clarifie le nombre de pages, les contenus disponibles, les besoins en referencement local et les demandes de formulaire ou galerie.

Validation humaine requise :
Oui

Prochaine action :
Envoyer un mini questionnaire de cadrage ou planifier un appel court de 15 a 20 minutes pour confirmer le nombre de pages, les contenus disponibles, la zone geographique cible, les references visuelles et le niveau d'urgence avant de preparer une estimation.
```

## Analyse qualite

### Points corrects

- la demande est bien reformulee en langage business simple
- les agents mobilises sont coherents avec le besoin
- le risque principal touche le vrai point critique : le faux cadrage
- la validation humaine est correctement exigee avant toute promesse
- la prochaine action est exploitable immediatement

### Limites observees

- la sortie ne donne pas de fourchette de prix, donc elle qualifie mais ne convertit pas encore
- l'agent ne distingue pas encore entre site vitrine tres simple et mini site avec SEO local plus pousse
- l'agent ne classe pas les informations a demander par ordre de criticite

## Analyse cout

Choix retenu : cloud OpenAI.

Hypothese raisonnable pour un run de qualification simple :

- 1 prompt systeme court
- 1 message utilisateur court
- 1 reponse courte

Impact cout :

- faible pour un usage manuel occasionnel
- variable si ce flux est industrialise a fort volume

Je ne fixe pas de montant exact ici car il depend du modele finalement choisi et de la tarification en vigueur au moment du deploiement. A verifier avant mise en production.

## Donnees exposees

Donnees potentiellement envoyees au fournisseur cloud :

- description libre du besoin prospect
- informations de contexte commercial
- eventuellement nom du prospect, secteur, localisation et contraintes de delai

Donnees a ne pas envoyer sans gouvernance claire :

- informations bancaires
- documents contractuels non expurges
- credentials
- donnees sensibles sans base legale ou consentement

## Prochaine amelioration

- ajouter une sortie optionnelle `informations manquantes`
- ajouter une fourchette de budget non engageante avec hypotheses explicites
- transformer la prochaine action en template de questionnaire de cadrage
- tester le meme prompt sur un second fournisseur pour comparer la discipline de sortie
