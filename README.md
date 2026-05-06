# TP : Mise en place d'une CI avec gestion de bibliothèque

Projet d'exercice en Python autour de la manipulation de livres, du stockage JSON et des tests automatisés avec `pytest`.

## Objectifs

- Comprendre la manipulation de données en Python
- Lire et écrire dans un fichier JSON
- Mettre en place des tests automatisés avec `pytest`
- Configurer un pipeline CI

## Contexte

Le projet contient les fichiers suivants :

- `library.py` : gestion des livres
- `storage.py` : gestion du JSON
- `main.py` : programme principal

Le code fourni est volontairement incomplet et doit être corrigé, testé puis automatisé.

## Travail demandé

### Partie 1 : Modification du code

#### Fichier `library.py`

```python
def ajouter_livre(bibliotheque, titre, auteur):
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            return False
    bibliotheque.append({
        "titre": titre,
        "auteur": auteur
    })
    return True


def supprimer_livre(bibliotheque, titre):
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            bibliotheque.remove(livre)
            return True
    return False


def rechercher_livre(bibliotheque, titre):
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            return livre
    return None
```

### Partie 2 : Gestion du stockage

#### Fichier `storage.py`

```python
import json
import os


def sauvegarder(bibliotheque, fichier):
    try:
        with open(fichier, "w") as f:
            json.dump(bibliotheque, f, indent=4)
    except Exception as e:
        print("Erreur sauvegarde :", e)


def charger(fichier):
    if not os.path.exists(fichier):
        return []
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except Exception:
        return []
```

### Partie 3 : Programme principal

#### Fichier `main.py`

```python
from library import ajouter_livre, supprimer_livre, rechercher_livre
from storage import sauvegarder, charger


def main():
    biblio = charger("data.json")
    ajouter_livre(biblio, "1984", "George Orwell")
    ajouter_livre(biblio, "Dune", "Frank Herbert")
    print("Bibliothèque :", biblio)
    livre = rechercher_livre(biblio, "1984")
    print("Recherche :", livre)
    supprimer_livre(biblio, "Dune")
    print("Après suppression :", biblio)
    sauvegarder(biblio, "data.json")


if __name__ == "__main__":
    main()
```

### Partie 4 : Tests automatisés

- Test local avec `pytest`

### Partie 5 : CI/CD

#### Fichier `.gitlab-ci.yml` à créer

```yaml
stages:
  - test

test_job:
  stage: test
  image: python:3.10
  script:
    - pip install pytest
    - pytest
```

### Partie 6 : Vérification

- Le pipeline est-il vert ?
- Tous les tests passent-ils ?

## Livrables

- `library.py` corrigé
- `storage.py` corrigé
- `main.py` fonctionnel
- `test_library.py`
- `test_storage.py`
- `.gitlab-ci.yml`
- Capture du pipeline

## Remarque

GitHub affichera automatiquement ce fichier comme page d'accueil du dépôt.