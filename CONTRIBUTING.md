# Contribution guidelines (draft)

## Prérequis
- Python 3.9+
- `r3xa-api` installé :
  ```bash
  python -m pip install "r3xa-api @ git+https://gitlab.com/photomechanics/R3XA_API.git@v1.5.4"
  ```

## Ajouter un item
1. Placer le JSON dans l’arborescence `registry/<domaine>/...` (imagerie, essais_meca, procedes, conventions).
2. Renseigner : `id`, `title`, `description`, `domain`, `status`, `provenance {author, lab, contact}`, `version`, `updated_at`.
3. Vérifier que les champs spécifiques au schéma R3XA sont conformes (units, dimensions, liens source/dataset, etc.).
4. Valider localement :
   ```bash
   python scripts/validate_all.py
   ```

## Statuts
- `proposed` : soumis, en discussion
- `recommended` : validé par les mainteneurs
- `deprecated` : obsolète, à ne plus utiliser

## Bonnes pratiques
- IDs stables (24 lettres minuscules).
- Pas de chemins absolus, pas de binaire.
- Documenter la provenance (fabricant, lien, note).
- Décrire les unités/dimensions quand pertinent.

## CI attendue
- Avant chaque merge request, exécuter `python scripts/validate_all.py`.
- L’automatisation CI du projet reste à configurer.

Merci !
