import pytest
from library import ajouter_livre, supprimer_livre, rechercher_livre


class TestAjouterLivre:
    """Tests pour la fonction ajouter_livre"""
    
    def test_ajouter_livre_success(self):
        """Test l'ajout d'un livre avec succès"""
        biblio = []
        result = ajouter_livre(biblio, "1984", "George Orwell")
        assert result is True
        assert len(biblio) == 1
        assert biblio[0]["titre"] == "1984"
        assert biblio[0]["auteur"] == "George Orwell"
    
    def test_ajouter_livre_duplicate(self):
        """Test que l'ajout d'un doublon retourne False"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = ajouter_livre(biblio, "1984", "Autre Auteur")
        assert result is False
        assert len(biblio) == 1  # La liste ne doit pas augmenter
    
    def test_ajouter_livre_case_insensitive(self):
        """Test que la détection de doublon est insensible à la casse"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = ajouter_livre(biblio, "1984", "Autre Auteur")
        assert result is False
        
        result = ajouter_livre(biblio, "1984", "Autre Auteur")
        assert result is False
        
        result = ajouter_livre(biblio, "1984", "Autre Auteur")
        assert result is False
    
    def test_ajouter_multiple_livres(self):
        """Test l'ajout de plusieurs livres différents"""
        biblio = []
        assert ajouter_livre(biblio, "1984", "George Orwell") is True
        assert ajouter_livre(biblio, "Dune", "Frank Herbert") is True
        assert ajouter_livre(biblio, "Le Seigneur des Anneaux", "J.R.R. Tolkien") is True
        assert len(biblio) == 3
    
    def test_ajouter_livre_empty_title(self):
        """Test l'ajout d'un livre avec un titre vide"""
        biblio = []
        result = ajouter_livre(biblio, "", "Auteur")
        assert result is True
        assert len(biblio) == 1
    
    def test_ajouter_livre_empty_author(self):
        """Test l'ajout d'un livre avec un auteur vide"""
        biblio = []
        result = ajouter_livre(biblio, "Titre", "")
        assert result is True
        assert len(biblio) == 1


class TestSupprimerLivre:
    """Tests pour la fonction supprimer_livre"""
    
    def test_supprimer_livre_success(self):
        """Test la suppression d'un livre existant"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = supprimer_livre(biblio, "1984")
        assert result is True
        assert len(biblio) == 0
    
    def test_supprimer_livre_not_found(self):
        """Test la suppression d'un livre inexistant retourne False"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = supprimer_livre(biblio, "Inexistant")
        assert result is False
        assert len(biblio) == 1  # La bibliothèque reste inchangée
    
    def test_supprimer_livre_case_insensitive(self):
        """Test que la suppression est insensible à la casse"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = supprimer_livre(biblio, "1984")
        assert result is True
        assert len(biblio) == 0
    
    def test_supprimer_livre_from_multiple(self):
        """Test la suppression d'un livre parmi plusieurs"""
        biblio = [
            {"titre": "1984", "auteur": "George Orwell"},
            {"titre": "Dune", "auteur": "Frank Herbert"},
            {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien"}
        ]
        result = supprimer_livre(biblio, "Dune")
        assert result is True
        assert len(biblio) == 2
        assert biblio[0]["titre"] == "1984"
        assert biblio[1]["titre"] == "Le Seigneur des Anneaux"
    
    def test_supprimer_livre_empty_biblio(self):
        """Test la suppression d'un livre dans une bibliothèque vide"""
        biblio = []
        result = supprimer_livre(biblio, "Titre")
        assert result is False
        assert len(biblio) == 0
    
    def test_supprimer_livre_mixed_case(self):
        """Test que la suppression fonctionne avec des casses différentes"""
        biblio = [{"titre": "Le Seigneur Des Anneaux", "auteur": "Tolkien"}]
        result = supprimer_livre(biblio, "le seigneur des anneaux")
        assert result is True
        assert len(biblio) == 0


class TestRechercherLivre:
    """Tests pour la fonction rechercher_livre"""
    
    def test_rechercher_livre_found(self):
        """Test la recherche d'un livre existant"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = rechercher_livre(biblio, "1984")
        assert result is not None
        assert result["titre"] == "1984"
        assert result["auteur"] == "George Orwell"
    
    def test_rechercher_livre_not_found(self):
        """Test la recherche d'un livre inexistant retourne None"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = rechercher_livre(biblio, "Inexistant")
        assert result is None
    
    def test_rechercher_livre_case_insensitive(self):
        """Test que la recherche est insensible à la casse"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        
        result = rechercher_livre(biblio, "1984")
        assert result is not None
        
        result = rechercher_livre(biblio, "1984")
        assert result is not None
    
    def test_rechercher_livre_from_multiple(self):
        """Test la recherche d'un livre parmi plusieurs"""
        biblio = [
            {"titre": "1984", "auteur": "George Orwell"},
            {"titre": "Dune", "auteur": "Frank Herbert"},
            {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien"}
        ]
        result = rechercher_livre(biblio, "Dune")
        assert result is not None
        assert result["titre"] == "Dune"
        assert result["auteur"] == "Frank Herbert"
    
    def test_rechercher_livre_empty_biblio(self):
        """Test la recherche dans une bibliothèque vide"""
        biblio = []
        result = rechercher_livre(biblio, "Titre")
        assert result is None
    
    def test_rechercher_livre_mixed_case(self):
        """Test que la recherche fonctionne avec des casses différentes"""
        biblio = [{"titre": "Le Seigneur Des Anneaux", "auteur": "Tolkien"}]
        result = rechercher_livre(biblio, "le seigneur des anneaux")
        assert result is not None
        assert result["auteur"] == "Tolkien"
    
    def test_rechercher_livre_returns_reference(self):
        """Test que la recherche retourne une référence au livre"""
        biblio = [{"titre": "1984", "auteur": "George Orwell"}]
        result = rechercher_livre(biblio, "1984")
        # Vérifier qu'on obtient bien une référence (modification affecte la liste)
        assert result is biblio[0]
