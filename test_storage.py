import pytest
import json
import os
import tempfile
from storage import sauvegarder, charger


class TestSauvegarder:
    """Tests pour la fonction sauvegarder"""
    
    def test_sauvegarder_create_file(self):
        """Test la création d'un fichier JSON"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            biblio = [{"titre": "1984", "auteur": "George Orwell"}]
            
            sauvegarder(biblio, fichier)
            
            assert os.path.exists(fichier)
            with open(fichier, "r") as f:
                data = json.load(f)
                assert data == biblio
    
    def test_sauvegarder_empty_library(self):
        """Test la sauvegarde d'une bibliothèque vide"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            biblio = []
            
            sauvegarder(biblio, fichier)
            
            assert os.path.exists(fichier)
            with open(fichier, "r") as f:
                data = json.load(f)
                assert data == []
    
    def test_sauvegarder_multiple_books(self):
        """Test la sauvegarde de plusieurs livres"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            biblio = [
                {"titre": "1984", "auteur": "George Orwell"},
                {"titre": "Dune", "auteur": "Frank Herbert"},
                {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien"}
            ]
            
            sauvegarder(biblio, fichier)
            
            with open(fichier, "r") as f:
                data = json.load(f)
                assert len(data) == 3
                assert data[0]["titre"] == "1984"
                assert data[1]["titre"] == "Dune"
                assert data[2]["titre"] == "Le Seigneur des Anneaux"
    
    def test_sauvegarder_overwrite_file(self):
        """Test que la sauvegarde écrase le fichier existant"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            # Première sauvegarde
            biblio1 = [{"titre": "1984", "auteur": "Orwell"}]
            sauvegarder(biblio1, fichier)
            
            # Seconde sauvegarde
            biblio2 = [{"titre": "Dune", "auteur": "Herbert"}]
            sauvegarder(biblio2, fichier)
            
            # Vérifier que seule la dernière sauvegarde est présente
            with open(fichier, "r") as f:
                data = json.load(f)
                assert len(data) == 1
                assert data[0]["titre"] == "Dune"
    
    def test_sauvegarder_format_indent(self):
        """Test que la sauvegarde utilise l'indentation correcte"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            biblio = [{"titre": "1984", "auteur": "Orwell"}]
            
            sauvegarder(biblio, fichier)
            
            with open(fichier, "r") as f:
                content = f.read()
                # Vérifier que le fichier est formaté avec indentation
                assert "    " in content  # Indentation de 4 espaces


class TestCharger:
    """Tests pour la fonction charger"""
    
    def test_charger_valid_file(self):
        """Test le chargement d'un fichier JSON valide"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            expected_data = [{"titre": "1984", "auteur": "George Orwell"}]
            
            with open(fichier, "w") as f:
                json.dump(expected_data, f)
            
            result = charger(fichier)
            assert result == expected_data
    
    def test_charger_file_not_found(self):
        """Test que charger retourne [] si le fichier n'existe pas"""
        result = charger("/nonexistent/path/to/file.json")
        assert result == []
    
    def test_charger_empty_file(self):
        """Test le chargement d'un fichier JSON vide (contenant [])"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            with open(fichier, "w") as f:
                json.dump([], f)
            
            result = charger(fichier)
            assert result == []
    
    def test_charger_multiple_books(self):
        """Test le chargement de plusieurs livres"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            expected_data = [
                {"titre": "1984", "auteur": "George Orwell"},
                {"titre": "Dune", "auteur": "Frank Herbert"},
                {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien"}
            ]
            
            with open(fichier, "w") as f:
                json.dump(expected_data, f)
            
            result = charger(fichier)
            assert len(result) == 3
            assert result[0]["titre"] == "1984"
            assert result[1]["titre"] == "Dune"
            assert result[2]["titre"] == "Le Seigneur des Anneaux"
    
    def test_charger_invalid_json(self):
        """Test que charger retourne [] si le JSON est invalide"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            with open(fichier, "w") as f:
                f.write("{'invalid': json}")
            
            result = charger(fichier)
            assert result == []
    
    def test_charger_corrupted_file(self):
        """Test que charger retourne [] si le fichier est corrompu"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            with open(fichier, "w") as f:
                f.write("not valid json at all")
            
            result = charger(fichier)
            assert result == []
    
    def test_charger_empty_json_object(self):
        """Test le chargement d'un objet JSON vide {}"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            with open(fichier, "w") as f:
                json.dump({}, f)
            
            # Note: json.load({}) retourne un dictionnaire, pas une liste
            result = charger(fichier)
            assert isinstance(result, dict)
    
    def test_charger_partial_json(self):
        """Test que charger retourne [] si le JSON est incomplet"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            with open(fichier, "w") as f:
                f.write('[{"titre": "1984",')  # JSON incomplet
            
            result = charger(fichier)
            assert result == []


class TestIntegration:
    """Tests d'intégration entre sauvegarder et charger"""
    
    def test_save_and_load_roundtrip(self):
        """Test que charger retrouve exactement ce qui a été sauvegardé"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            original_data = [
                {"titre": "1984", "auteur": "George Orwell"},
                {"titre": "Dune", "auteur": "Frank Herbert"}
            ]
            
            sauvegarder(original_data, fichier)
            loaded_data = charger(fichier)
            
            assert loaded_data == original_data
    
    def test_multiple_save_and_load_cycles(self):
        """Test plusieurs cycles de sauvegarde et chargement"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fichier = os.path.join(tmpdir, "test.json")
            
            # Cycle 1
            data1 = [{"titre": "Livre 1", "auteur": "Auteur 1"}]
            sauvegarder(data1, fichier)
            loaded1 = charger(fichier)
            assert loaded1 == data1
            
            # Cycle 2
            data2 = [
                {"titre": "Livre 1", "auteur": "Auteur 1"},
                {"titre": "Livre 2", "auteur": "Auteur 2"}
            ]
            sauvegarder(data2, fichier)
            loaded2 = charger(fichier)
            assert loaded2 == data2
