# Tool Catalog

## Intention

Ce catalogue formalise les actions activables du Founder OS pour eviter deux erreurs frequentes :

- confondre un agent avec une action executable ;
- laisser des sorties floues qui ne peuvent ni etre testees ni etre controlees.

## Catalogue

| Action | Mission | Agents autorises | Entrees | Sortie attendue | Permissions | Risques | Approval requis | Stack utilisee |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `qualify_lead` | Qualifier une demande entrante en besoin, risque, agents a mobiliser et prochaine action. | Agent Prospection, Agent Coach | message prospect, source, contexte commercial | qualification structuree de lead | lecture seule sur brief et docs internes | mauvaise qualification, promesse prematuree sur prix/delai | Oui si la sortie engage un prix, un delai ou un contact externe | locale |
| `draft_email_reply` | Rediger un brouillon de reponse commerciale prudent et contextualise. | Agent Mail / Sales | fiche prospect, angle de reponse, objection, CTA souhaite | brouillon de mail structure | brouillon uniquement, aucun envoi | ton inapproprie, engagement commercial non valide, fuite de contexte client | Oui avant tout envoi reel | no-code `n8n` ou simulee |
| `create_mock_quote` | Produire un devis fictif a valeur pedagogique ou de pre-cadrage. | Agent Admin / Compta | nom du client, perimetre MVP, options, hypothese budget | devis fictif avec total indicatif et hypotheses | document non contractuel, pas d'emission client | confusion entre devis brouillon et engagement ferme | Oui si conversion en devis final ou partage externe | locale ou simulee |
| `extract_seo_keywords` | Extraire une premiere liste de mots-cles et intentions de recherche a partir d'un brief. | Agent SEO | activite, zone geographique, offre, site ou texte source | liste priorisee de mots-cles et intentions | lecture/analyse uniquement | recommandations trop generiques, mauvais ciblage local | Non pour analyse interne, Oui si usage d'API payante SEO | simulee, locale ou cloud/API |
| `search_knowledge_base` | Rechercher une information dans la memoire locale, les SOP et la documentation du repo. | Agent Coach, Agent Code / Produit, Agent Prospection, Agent Admin / Compta | question, mot-cle, dossier cible | resultat de recherche structure avec sources | lecture locale uniquement | faux positif, mauvaise citation, oubli de source | Non | locale |
| `write_note_draft` | Preparer une note de synthese avant ecriture durable dans le vault. | Agent Coach, Agent Code / Produit, Agent Mail / Sales | titre, contenu source, type de note, destination | note brouillon markdown | brouillon autorise, ecriture permanente controlee | pollution de la memoire durable, mauvaise classification | Oui si ecriture permanente dans Obsidian/vault | locale |
| `summarize_call_notes` | Transformer des notes brutes d'appel en synthese actionnable. | Agent Mail / Sales, Agent Coach | notes d'appel, decisions, questions ouvertes | recap de call avec actions et risques | lecture et redaction interne | oubli d'un engagement, mauvaise interpretation | Oui si la synthese est envoyee au client telle quelle | simulee ou locale |

## Notes de design

- Une action doit avoir une sortie testable. Sinon ce n'est pas une action exploitable.
- Les actions `draft_email_reply` et `write_note_draft` restent en mode brouillon par defaut. C'est un garde-fou, pas une limitation cosmetique.
- `create_mock_quote` est volontairement non contractuel. Si tu sautes cette distinction, tu melanges assistance operationnelle et engagement legal.

## Bonus day 2

Un workflow `n8n` importable existe maintenant pour `draft_email_reply` dans `automations/n8n/draft-email-reply-workflow.json`. Il formalise le passage du contrat d'interface a une premiere automatisation no-code versionnee.
