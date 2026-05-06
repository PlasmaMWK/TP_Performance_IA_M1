import json
import os


def sauvegarder(bibliotheque, fichier):
    """
    Sauvegarde la bibliothèque dans un fichier JSON.
    
    Args:
        bibliotheque (list): Liste de dictionnaires de livres à sauvegarder
        fichier (str): Chemin du fichier JSON de destination
        
    Raises:
        Exception: En cas d'erreur lors de l'écriture
    """
    try:
        with open(fichier, "w") as f:
            json.dump(bibliotheque, f, indent=4)
    except Exception as e:
        print("Erreur sauvegarde :", e)


def charger(fichier):
    """
    Charge la bibliothèque depuis un fichier JSON.
    Retourne une liste vide si le fichier n'existe pas ou en cas d'erreur.
    
    Args:
        fichier (str): Chemin du fichier JSON à charger
        
    Returns:
        list: La liste de livres chargée ou [] si erreur/fichier absent
    """
    if not os.path.exists(fichier):
        return []
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except Exception:
        return []
