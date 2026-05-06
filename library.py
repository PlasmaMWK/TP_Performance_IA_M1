def ajouter_livre(bibliotheque, titre, auteur):
    """
    Ajoute un livre à la bibliothèque si le titre n'existe pas déjà.
    
    Args:
        bibliotheque (list): Liste de dictionnaires de livres
        titre (str): Titre du livre à ajouter
        auteur (str): Auteur du livre à ajouter
        
    Returns:
        bool: True si le livre a été ajouté, False si un doublon existe
    """
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            return False
    bibliotheque.append({
        "titre": titre,
        "auteur": auteur
    })
    return True


def supprimer_livre(bibliotheque, titre):
    """
    Supprime un livre de la bibliothèque par son titre.
    
    Args:
        bibliotheque (list): Liste de dictionnaires de livres
        titre (str): Titre du livre à supprimer
        
    Returns:
        bool: True si le livre a été supprimé, False si non trouvé
    """
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            bibliotheque.remove(livre)
            return True
    return False


def rechercher_livre(bibliotheque, titre):
    """
    Recherche un livre dans la bibliothèque par son titre.
    
    Args:
        bibliotheque (list): Liste de dictionnaires de livres
        titre (str): Titre du livre à rechercher
        
    Returns:
        dict: Le dictionnaire du livre si trouvé, None sinon
    """
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            return livre
    return None
