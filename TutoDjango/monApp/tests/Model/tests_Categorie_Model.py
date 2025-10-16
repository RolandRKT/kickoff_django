"""
Module de tests unitaires pour le modèle `Categorie`.

Ce fichier contient une série de tests qui valident le cycle de vie complet
d'une instance du modèle `Categorie` :
    - Création de l'objet
    - Représentation en chaîne (__str__)
    - Mise à jour d'un champ
    - Suppression de l'objet

Les tests utilisent la base de données de test intégrée de Django,
ce qui signifie qu'ils sont isolés et n'affectent pas la base réelle.
"""

from django.test import TestCase
from monApp.models import Categorie


class CategorieModelTest(TestCase):
    """
    Classe de tests pour le modèle `Categorie`.

    Hérite de `django.test.TestCase`, qui met en place une base de données
    temporaire pour exécuter les tests de manière isolée et automatique.
    """

    def setUp(self):
        """
        Méthode exécutée avant chaque test.

        Elle permet de créer une instance `Categorie` de test afin
        de ne pas répéter le code d'initialisation dans chaque méthode.
        """
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")

    def test_categorie_creation(self):
        """
        Vérifie que la création d'une catégorie fonctionne correctement.

        Attendu :
            - L'attribut `nomCat` de l'objet créé correspond à la valeur initiale.
        """
        self.assertEqual(self.ctgr.nomCat, "CategoriePourTest")

    def test_string_representation(self):
        """
        Vérifie la méthode __str__ du modèle `Categorie`.

        Attendu :
            - La conversion en chaîne de l'objet doit renvoyer la valeur de `nomCat`.
        """
        self.assertEqual(str(self.ctgr), "CategoriePourTest")

    def test_categorie_updating(self):
        """
        Vérifie la mise à jour d'un enregistrement existant.

        Étapes :
            1. Modifier `nomCat`
            2. Sauvegarder les changements
            3. Récupérer l'objet en base
            4. Vérifier que le champ a bien été mis à jour
        """
        self.ctgr.nomCat = "CategoriePourTests"
        self.ctgr.save()

        # Récupérer l'objet mis à jour depuis la base
        updated_ctgr = Categorie.objects.get(idCat=self.ctgr.idCat)
        self.assertEqual(updated_ctgr.nomCat, "CategoriePourTests")

    def test_categorie_deletion(self):
        """
        Vérifie la suppression d'une catégorie.

        Étapes :
            1. Supprimer l'objet
            2. Vérifier que la table ne contient plus aucune instance
        """
        self.ctgr.delete()
        self.assertEqual(Categorie.objects.count(), 0)
