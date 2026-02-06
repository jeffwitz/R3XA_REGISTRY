# Cahier des charges (principes)

## Référentiels partagés pour la description du matériel et des expériences

### Objectif du document

Ce document vise à **poser les principes** d’un référentiel partagé (registry) pour décrire du matériel, des procédés et des conventions dans un cadre inter-laboratoires.

Il ne s’agit **pas** :

* de décider d’un outil,
* ni d’imposer une organisation existante,
* ni de figer une ontologie.

Il s’agit de **clarifier les options**, leurs implications, et leur compatibilité avec le format R3XA.


## 1. Intuition de départ

Dans un projet inter-laboratoires, la question centrale n’est généralement pas :

> *« À quel labo appartient ce matériel ? »*

mais plutôt :

> *« De quel type de matériel s’agit-il, et comment est-il décrit ? »*

Le laboratoire est une **information contextuelle**, utile pour l’usage ou l’inventaire,
mais pas forcément une **clé de classification conceptuelle**.



## 2. Principe fondamental proposé

> **La classification doit refléter la nature et l’usage des objets,
> pas leur appartenance institutionnelle.**

Autrement dit :

* la **sémantique** (ce que c’est) doit être séparée
* de la **provenance** (qui l’a décrit, maintient ou utilise)


## 3. Trois dimensions à distinguer clairement

Pour éviter les confusions, il est utile de distinguer trois dimensions indépendantes.

### 3.1 Structure (le “type”)

* Quelle est la **forme** de l’objet ?
* Exemples : caméra, machine d’essai, jeu de données, procédé.

👉 Cette dimension est **structurelle** et stable.
Elle est déjà bien couverte par le format R3XA.


### 3.2 Nature / domaine (le “quoi”)

* De quoi parle-t-on ?
* Exemples :

  * imagerie
  * essais mécaniques
  * procédés thermiques
  * métadonnées et conventions

-> C’est une **classification par usage et sens**, indépendante du lieu.



### 3.3 Provenance / responsabilité (le “qui”)

* Qui a proposé ou maintient cette description ?
* Qui la recommande ?
* Où est-elle utilisée ?

-> Cette dimension est **organisationnelle**, pas sémantique.



## 4. Compatibilité avec le format R3XA

Point clé pour la discussion :

> **Ces principes sont compatibles avec le format R3XA actuel.**

Pourquoi ?

* R3XA décrit déjà :

  * des **types d’objets** (via le schéma),
  * des **instances** (dans les fichiers d’expérience).
* Le format n’impose **aucune ontologie rigide** sur la classification.
* Les notions de “registry”, “catalogue” ou “référentiel” sont **au-dessus du format**, pas à l’intérieur.

👉 Autrement dit :

* R3XA peut **accueillir** plusieurs stratégies de registry,
* sans modifier sa structure fondamentale.



## 5. Options de structuration des registries (à discuter)

### Option A — Registries par laboratoire

Chaque laboratoire maintient son propre registry.

**Avantages**

* simple à démarrer
* autonomie locale
* faible gouvernance

**Inconvénients**

* classification peu naturelle pour l’utilisateur
* duplication probable (même matériel décrit plusieurs fois)
* difficile de parler de “référentiel commun”

👉 Option pragmatique, mais peu satisfaisante conceptuellement.



### Option B — Registries par nature / domaine (proposition centrale)

Les registries sont organisés par **thématique** :

* imagerie
* essais mécaniques
* procédés
* conventions

Les laboratoires deviennent :

* contributeurs
* mainteneurs
* utilisateurs

**Avantages**

* classification intuitive
* favorise la convergence
* reflète mieux les usages réels
* donne une “stature” de référentiel

**Inconvénients**

* nécessite un minimum de coordination
* demande d’expliciter des règles de contribution

👉 Option conceptuellement la plus cohérente pour un projet inter-labos.



### Option C — Registry unique fédéré

Un registre commun unique, avec :

* des tags de domaine
* des métadonnées de provenance

**Avantages**

* un seul point d’entrée
* vision globale

**Inconvénients**

* peut devenir lourd
* nécessite une gouvernance claire
* risque de dilution si mal cadré

-> Option possible si la communauté est prête à maintenir un socle commun.



## 6. Cas clé : “le même matériel dans plusieurs labos”

Principe important :

> Deux laboratoires peuvent utiliser le **même type de matériel**
> sans que cela pose un problème conceptuel.

Cela implique de distinguer :

* le **modèle / type** (commun)
* l’**exemplaire concret** (local)

Le référentiel porte surtout sur le **premier**.



## 7. Ce qui donne une “vraie stature” à un registry

Indépendamment de l’option choisie, un référentiel prend de la valeur s’il a :

1. une **classification par nature**, compréhensible
2. des **statuts** (proposé, recommandé, obsolète)
3. une **traçabilité** (qui maintient, qui a contribué)
4. une **évolution explicite** (versions, discussions)

👉 La stature vient plus des **règles collectives** que de la technologie.



## 8. Questions ouvertes pour la discussion Photomeca

Pour lancer l’échange :

1. Quelle classification est la plus naturelle pour nous :
   par laboratoire ou par nature ?
2. Souhaite-t-on un ou plusieurs référentiels communs ?
3. Quel niveau de coordination est acceptable ?
4. Qu’est-ce qui doit être **commun** ?
   Qu’est-ce qui doit rester **local** ?
5. À partir de quand considère-t-on qu’une description est “de référence” ?



## 9. Phrase de synthèse

> *Un référentiel utile ne dit pas à qui appartient le matériel,
> mais ce que c’est, comment il est décrit,
> et comment on peut s’y référer collectivement.*

## 10. Décision proposée (mise en route)

**Option B — Registry par nature/domaine**, avec métadonnées de provenance. Concrètement :

- Arborescence par usage/sens (imagerie, essais mécaniques, procédés, conventions), pas par labo.
- Chaque entrée JSON contient aussi la provenance (auteur/labo/contact) et un statut.
- Les labos restent contributeurs/mainteneurs, mais la classification reste sémantique.

## 11. Métadonnées minimales pour chaque entrée

Dans chaque JSON (réutilisable avec `validate_item` de R3XA_API) :

- `id` : 24 lettres minuscules, stable
- `title`, `description`
- `domain` : imagerie | essais_meca | procedes | conventions
- `status` : proposed | recommended | deprecated
- `provenance` : { author, lab, contact }
- `version`, `updated_at`

## 12. Structure de dépôt proposée

```
registry/
  imagerie/
    data_sources/
      camera/
        avt_dolphin_f145b.json
    data_sets/
      dic/
        displacement_field.json
  essais_meca/
    settings/
      specimen/
        openhole_sample.json
    machines/
      tensile_frame_mts.json
  procedes/
  conventions/
scripts/
  validate_all.py
```

## 13. Règles de contribution (brouillon)

- JSON valide, minimal, sans chemins absolus ni binaire.
- `id` unique, statut renseigné, provenance renseignée.
- `validate_item` doit passer (schema R3XA).
- Décrire les unités/dimensions pertinentes.
- PR acceptée après validation CI.

## 14. Automatisation

- Script `scripts/validate_all.py` pour parcourir `registry/` et appeler `validate_item`.
- GitHub Actions : `pip install r3xa-api` puis `python scripts/validate_all.py` sur chaque PR.

## 15. Prochaines étapes

1. Initialiser l’arborescence vide (domains) et le script de validation.
2. Migrer 2–3 items phares (caméra AVT, specimen openhole, dataset DIC) comme exemples.
3. Rédiger un `CONTRIBUTING.md` court et un gabarit JSON.
4. Tag v0.1 du registry une fois les premiers items validés.
