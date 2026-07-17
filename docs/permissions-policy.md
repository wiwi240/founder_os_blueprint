# Permissions Policy

## Principe

Par defaut, toute action ayant un impact externe, financier, irreversible ou legal demande une validation humaine explicite.

Le mode par defaut du Founder OS est le brouillon interne. Une action qui sort de ce mode doit etre traitee comme sensible.

## Regles

| Action sensible | Statut | Commentaire |
| --- | --- | --- |
| Rediger un brouillon d'email | Autorisee | Brouillon interne uniquement, aucun envoi |
| Envoyer un email reel | Autorisee seulement avec validation humaine | Impact externe direct |
| Ecrire un brouillon de note pour le vault | Autorisee | Brouillon local modifiable avant classement |
| Ecrire dans une note permanente du vault | Autorisee seulement avec validation humaine | Evite de polluer la memoire durable |
| Modifier un fichier projet | Autorisee | Autorise dans le cadre du repo courant et avec trace |
| Supprimer un fichier projet | Autorisee seulement avec validation humaine | Action potentiellement irreversible |
| Generer un devis brouillon fictif | Autorisee | Pas de valeur contractuelle, usage interne ou pedagogique |
| Emettre un devis final | Autorisee seulement avec validation humaine | Engage l'activite commerciale |
| Utiliser une API payante | Autorisee seulement avec validation humaine | Impact budget, doit etre signale explicitement avant usage |
| Importer des donnees prospects | Autorisee seulement avec validation humaine | Risque legal et qualite de donnees |
| Exporter des donnees clients | Autorisee seulement avec validation humaine | Sensibilite des informations |
| Publier sur un site en production | Interdite | Hors scope day 1 |
| Acceder a des identifiants ou secrets | Interdite | A gerer via systemes separes et securises |
| Lancer un script local de generation de documents | Autorisee | Si le script est versionne et auditable |

## Regles complementaires day 2

- Les mails sont en brouillon uniquement tant qu'un humain n'a pas valide le contenu et l'intention d'envoi.
- Les devis produits par le systeme sont fictifs par defaut et doivent afficher explicitement leur caractere non contractuel.
- L'ecriture dans Obsidian ou dans toute memoire permanente demande validation humaine prealable.
- Toute API payante doit etre signalee avant usage avec impact attendu sur le budget et justification.
- Toute action cloud qui expose des donnees client doit documenter les donnees envoyees et la finalite.

## Niveau de controle attendu

- Lecture/analyse : souvent autorisee
- Redaction de brouillons : generalement autorisee
- Ecriture persistante : controlee
- Actions externes : controle humain quasi systematique
- Actions financieres ou legales : validation humaine obligatoire
