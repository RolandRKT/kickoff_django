"""
Module de tests unitaires pour le formulaire `CategorieForm`.

Ce fichier contient des tests pour vérifier le comportement du formulaire
`CategorieForm` de l'application `monApp`, notamment :
    - Validation de données correctes
    - Validation de données trop longues
    - Validation de champs manquants
    - Sauvegarde en base d'une catégorie valide
"""

from django.test import TestCase
from monApp.form import CategorieForm
from monApp.models import Categorie


class CategorieFormTest(TestCase):
    """
    Classe de tests pour le formulaire `CategorieForm`.

    Chaque méthode teste un aspect différent de la validation ou de la
    sauvegarde du formulaire.
    """

    def test_form_valid_data(self):
        """
        Vérifie que le formulaire est valide lorsque toutes les données
        requises sont correctement fournies.

        Attendu :
            - Le formulaire doit être valide (is_valid() == True)
        """
        form = CategorieForm(data={'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())
        
    def test_form_valid_data_too_long(self):
        """
        Vérifie le comportement du formulaire lorsque la valeur fournie
        dépasse la longueur maximale autorisée.

        Étapes :
            1. Créer une chaîne trop longue pour `nomCat`
            2. Vérifier que le formulaire est invalide
            3. Vérifier qu'une erreur est présente pour le champ `nomCat`
            4. Vérifier que le message d'erreur mentionne la limite
        """
        # Crée une valeur de 102 caractères (trop longue si max_length=100)
        too_long_value = ("CategoriePourTest" * 10)[:102]

        form = CategorieForm(data={'nomCat': too_long_value})

        # Le formulaire doit être invalide
        self.assertFalse(form.is_valid())

        # Le champ 'nomCat' doit contenir une erreur
        self.assertIn('nomCat', form.errors)

        # Le message d'erreur peut varier selon la locale, donc on vérifie
        # qu'il mentionne la limite "100" ou "au plus 100"
        error_text = form.errors['nomCat'][0]
        self.assertTrue(
            ('100' in error_text) or ('au plus 100' in error_text),
            msg=f"Message d'erreur inattendu: {error_text}"
        )

    def test_form_valid_data_missed(self):
        """
        Vérifie le comportement du formulaire lorsque le champ `nomCat`
        est laissé vide.

        Attendu :
            - Le formulaire doit être invalide
            - Une erreur doit être présente pour le champ `nomCat`
            - Le message d'erreur doit indiquer que le champ est obligatoire
        """
        form = CategorieForm(data={'nomCat': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('nomCat', form.errors) # Le champ 'nomCat' doit contenir une erreur
        self.assertEqual(form.errors['nomCat'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        """
        Vérifie que le formulaire peut sauvegarder correctement une
        catégorie valide en base de données.

        Étapes :
            1. Fournir des données valides au formulaire
            2. Vérifier que le formulaire est valide
            3. Sauvegarder l'objet et vérifier ses attributs
        """
        form = CategorieForm(data={'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())
        ctgr = form.save()

        # Vérifie que les attributs de l'objet sauvegardé sont corrects
        self.assertEqual(ctgr.nomCat, 'CategoriePourTest')
        self.assertEqual(ctgr.idCat, 1)
