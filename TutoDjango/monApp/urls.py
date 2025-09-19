from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(template_name="monApp/page_home.html")),
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("aboutus/", views.AboutView.as_view(), name="aboutus"),

    # PRODUITS
    path("produits/", views.ProduitListView.as_view(), name="lst_prdts"),
    path("produit/<pk>/", views.ProduitDetailView.as_view(), name="dtl_prdt"),

    # CATEGORIES
    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path("categorie/<pk>/", views.CategorieDetailView.as_view(), name="dtl_cat"),

    # STATUTS
    path("statuts/", views.StatutListView.as_view(), name="lst_status"),
    path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_statut"),

    # RAYONS
    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),

    path("ma_vue/", views.ma_vue, name="ma_vuuue"),
]
