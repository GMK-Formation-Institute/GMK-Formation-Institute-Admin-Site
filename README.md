# Espace de gestion — IGMK Formation (maquette)

Maquette interactive de l'espace de gestion de l'Institut GMK Formation : élèves, inscriptions, paiements,
personnel, statistiques, contenu du site public.

**Toutes les données affichées sont fictives.** Aucune connexion réelle, aucune base de données :
les actions (ajouts, modifications, envois) sont simulées dans le navigateur et disparaissent au rechargement.

## Pages

| Rubrique | Pages |
|---|---|
| Connexion | `index.html` |
| Pilotage | `dashboard.html`, `eleves.html`, `eleve.html`, `preinscriptions.html`, `inscriptions.html`, `paiements.html`, `stats.html`, `stages.html` |
| École | `classes.html`, `emploi.html`, `personnel.html`, `membre.html`, `certificats.html` |
| Site public | `actualites.html`, `site.html` |
| Compte | `journal.html`, `parametres.html` |

Une barre en bas de l'écran permet de passer d'une page à l'autre, et une seconde de changer de palette de couleurs
(`?palette=3`, `4` ou `5` dans l'adresse).

## Voir en local

```bash
python3 -m http.server 8000
```

## Modifier

Les pages sont générées par `build.py` (gabarits dans `_src/`, styles dans `style.css`, comportements dans les fichiers `.js`) :

```bash
python3 build.py
```
