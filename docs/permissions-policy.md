# Permissions Policy

## Principe

Par defaut, toute action ayant un impact externe, financier, irreversible ou legal demande une validation humaine explicite.

## Regles

| Action sensible | Statut | Commentaire |
| --- | --- | --- |
| Envoyer un email reel | Autorisee seulement avec validation humaine | Impact externe direct |
| Ecrire dans une note permanente du vault | Autorisee seulement avec validation humaine | Evite de polluer la memoire durable |
| Modifier un fichier projet | Autorisee | Autorise dans le cadre du repo courant et avec trace |
| Supprimer un fichier projet | Autorisee seulement avec validation humaine | Action potentiellement irreversible |
| Generer un devis brouillon | Autorisee | Pas de valeur contractuelle tant que non valide |
| Emettre un devis final | Autorisee seulement avec validation humaine | Engage l'activite commerciale |
| Utiliser une API payante | Autorisee seulement avec validation humaine | Impact budget |
| Importer des donnees prospects | Autorisee seulement avec validation humaine | Risque legal et qualite de donnees |
| Exporter des donnees clients | Autorisee seulement avec validation humaine | Sensibilite des informations |
| Publier sur un site en production | Interdite | Hors scope day 1 |
| Acceder a des identifiants ou secrets | Interdite | A gerer via systemes separes et securises |
| Lancer un script local de generation de documents | Autorisee | Si le script est versionne et auditable |

## Niveau de controle attendu

- Lecture/analyse : souvent autorisee
- Redaction de brouillons : generalement autorisee
- Ecriture persistante : controlee
- Actions externes : controle humain quasi systematique
- Actions financieres ou legales : validation humaine obligatoire
