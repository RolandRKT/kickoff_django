"""
Module de tests unitaires pour les vues CRUD liées au modèle `Categorie`.

Ce fichier contient les tests des vues de création, détail, mise à jour et suppression
d'une catégorie. Les tests vérifient :
    - Le code HTTP des réponses GET et POST
    - Les templates utilisés
    - La création, mise à jour et suppression effective des objets
    - Les redirections après actions
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from monApp.models import Categorie


class CategorieCreateViewTest(TestCase):
    """
    Tests pour la vue de création d'une catégorie (CategorieCreateView).

    Vérifie le chargement du formulaire GET, la soumission POST et la création effective
    de l'objet en base.
    """

    def setUp(self):
        """
        Prépare un utilisateur connecté pour les tests nécessitant l'authentification.
        """
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_create_view_get(self):
        """
        Vérifie que l'accès à la vue de création renvoie un code 200
        et utilise le template correct.
        """
        response = self.client.get(reverse('crt_cat'))  # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_categorie.html')

    def test_categorie_create_view_post_valid(self):
        """
        Vérifie la création d'une catégorie via POST et la redirection.
        """
        data = {"nomCat": "CategoriePourTestCreation"}
        response = self.client.post(reverse('crt_cat'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Categorie.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Categorie.objects.last().nomCat, 'CategoriePourTestCreation')


class CategorieDetailViewTest(TestCase):
    """
    Tests pour la vue de détail d'une catégorie (CategorieDetailView).

    Vérifie que les informations de la catégorie sont correctement affichées.
    Aucune authentification requise ici.
    """

    def setUp(self):
        """
        Création d'une catégorie de test pour la consultation.
        """
        self.ctgr = Categorie.objects.create(nomCat="Cette catégorie contient")

    def test_categorie_detail_view(self):
        """
        Vérifie l'accès au détail d'une catégorie existante et l'affichage correct.
        """
        response = self.client.get(reverse('dtl_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_categorie.html')
        # Vérifie que le nom de la categorie est affiché
        self.assertContains(response, 'Cette catégorie contient')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, str(self.ctgr.idCat))


class CategorieUpdateViewTest(TestCase):
    """
    Tests pour la vue de mise à jour d'une catégorie (CategorieUpdateView).

    Vérifie à la fois le chargement du formulaire GET et la soumission POST.
    Authentification requise.
    """

    def setUp(self):
        """
        Création d'une catégorie et d'un utilisateur connecté.
        """
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_update_view_get(self):
        """
        Vérifie l'accès au formulaire de mise à jour et le template utilisé.
        """
        response = self.client.get(reverse('upd_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_categorie.html')

    def test_update_view_post_valid(self):
        """
        Vérifie la mise à jour effective d'une catégorie via POST.
        """
        self.assertEqual(self.ctgr.nomCat, 'CategoriePourTestUpdate')
        data = {'nomCat': 'CategoriePourTestAfterUpdate'}
        response = self.client.post(reverse('upd_cat', args=[self.ctgr.idCat]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.ctgr.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.ctgr.nomCat, 'CategoriePourTestAfterUpdate')


class CategorieDeleteViewTest(TestCase):
    """
    Tests pour la vue de suppression d'une catégorie (CategorieDeleteView).

    Vérifie que la suppression fonctionne et redirige correctement.
    Authentification requise.
    """

    def setUp(self):
        """
        Création d'une catégorie et d'un utilisateur connecté.
        """
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTesDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_delete_view_get(self):
        """
        Vérifie l'accès à la confirmation de suppression et le template utilisé.
        """
        response = self.client.get(reverse('dlt_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_categorie.html')

    def test_categorie_delete_view_post(self):
        """
        Vérifie la suppression effective d'une catégorie et la redirection.
        """
        response = self.client.post(reverse('dlt_cat', args=[self.ctgr.idCat]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Categorie.objects.filter(idCat=self.ctgr.idCat).exists())
        # Vérifier que la redirection est vers la liste des catégories
        self.assertRedirects(response, reverse('lst_cats'))
