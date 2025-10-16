"""
Module de tests unitaires pour les URLs liées au modèle `Categorie`.

Ce fichier contient des tests pour vérifier que les URLs définies dans
`monApp.urls` sont correctement résolues et pointent vers les vues
appropriées. Chaque test utilise `reverse` pour générer l'URL et
`resolve` pour obtenir la vue correspondante. Il teste également les
codes HTTP des réponses et les redirections après création, mise à
jour et suppression d'une catégorie.
"""

from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Categorie
from django.contrib.auth.models import User
from monApp.views import (
    CategorieListView,
    CategorieDetailView,
    CategorieCreateView,
    CategorieUpdateView,
    CategorieDeleteView,
)


class CategorieUrlsTest(TestCase):
    """
    Classe de tests pour vérifier la résolution des URLs et le comportement
    des vues CRUD de `Categorie`.

    Les tests incluent :
        - La résolution des URLs via `reverse` et `resolve`
        - La vérification du code HTTP des réponses GET
        - Les redirections après POST (création, mise à jour, suppression)
        - La gestion des objets non existants (404)
    """

    def setUp(self):
        """
        Prépare les données de test et l'utilisateur connecté.

        - Création d'une catégorie de test
        - Création et login d'un utilisateur
        """
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_list_url_is_resolved(self):
        """
        Vérifie que l'URL de la liste des catégories est correctement résolue.

        Étapes :
            1. Générer l'URL avec `reverse`
            2. Vérifier que le nom de l'URL est correct
            3. Vérifier que la vue associée est `CategorieListView`
        """
        url = reverse('lst_cats')
        self.assertEqual(resolve(url).view_name, 'lst_cats')
        self.assertEqual(resolve(url).func.view_class, CategorieListView)

    def test_categorie_detail_url_is_resolved(self):
        """
        Vérifie que l'URL de détail d'une catégorie est correctement résolue.
        """
        url = reverse('dtl_cat', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'dtl_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)

    def test_categorie_create_url_is_resolved(self):
        """
        Vérifie que l'URL de création d'une catégorie est correctement résolue.
        """
        url = reverse('crt_cat')
        self.assertEqual(resolve(url).view_name, 'crt_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)

    def test_categorie_update_url_is_resolved(self):
        """
        Vérifie que l'URL de modification d'une catégorie est correctement résolue.
        """
        url = reverse('upd_cat', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'upd_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)

    def test_categorie_delete_url_is_resolved(self):
        """
        Vérifie que l'URL de suppression d'une catégorie est correctement résolue.
        """
        url = reverse('dlt_cat', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'dlt_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)

    def test_categorie_list_response_code(self):
        """
        Vérifie que l'accès à la liste des catégories renvoie un code HTTP 200.
        """
        response = self.client.get(reverse('lst_cats'))
        self.assertEqual(response.status_code, 200)

    def test_categorie_detail_response_code(self):
        """
        Vérifie que l'accès au détail d'une catégorie existante renvoie un code 200.
        """
        url = reverse('dtl_cat', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_detail_response_code_KO(self):
        """
        Vérifie que l'accès au détail d'une catégorie inexistante renvoie un code 404.
        """
        url = reverse('dtl_cat', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_categorie_create_response_code_OK(self):
        """
        Vérifie que l'accès à la vue de création d'une catégorie renvoie un code 200.
        """
        response = self.client.get(reverse('crt_cat'))
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_response_code_OK(self):
        """
        Vérifie que l'accès à la vue de modification d'une catégorie existante renvoie un code 200.
        """
        url = reverse('upd_cat', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_response_code_KO(self):
        """
        Vérifie que l'accès à la vue de modification d'une catégorie inexistante renvoie un code 404.
        """
        url = reverse('upd_cat', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_categorie_delete_response_code_OK(self):
        """
        Vérifie que l'accès à la vue de suppression d'une catégorie existante renvoie un code 200.
        """
        url = reverse('dlt_cat', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_delete_response_code_KO(self):
        """
        Vérifie que l'accès à la vue de suppression d'une catégorie inexistante renvoie un code 404.
        """
        url = reverse('dlt_cat', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_redirect_after_categorie_creation(self):
        """
        Vérifie que la création d'une catégorie redirige correctement vers la vue de détail.
        """
        response = self.client.post(reverse('crt_cat'), {'nomCat': 'CategoriePourTestRedirectionCreation'})
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail : pk=2 (premier créé = 1, second = 2)
        self.assertRedirects(response, '/monApp/categorie/2/')

    def test_redirect_after_categorie_updating(self):
        """
        Vérifie que la mise à jour d'une catégorie redirige correctement vers la vue de détail.
        """
        response = self.client.post(reverse('upd_cat', args=[self.ctgr.idCat]),
                                    data={"nomCat": "CategoriePourTestRedirectionMaj"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/monApp/categorie/{self.ctgr.idCat}/')

    def test_redirect_after_categorie_deletion(self):
        """
        Vérifie que la suppression d'une catégorie redirige vers la liste et supprime l'objet.
        """
        response = self.client.post(reverse('dlt_cat', args=[self.ctgr.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lst_cats'))
        # Vérifie que la catégorie a bien été supprimée de la base
        self.assertFalse(Categorie.objects.filter(pk=self.ctgr.pk).exists())
