from library import ajouter_livre, supprimer_livre, rechercher_livre
from storage import sauvegarder, charger


def main():
    """
    Programme principal qui démontre l'utilisation du système de gestion de bibliothèque.
    """
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
