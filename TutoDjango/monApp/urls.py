from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
    # LOGIN
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path("home/", views.HomeView.as_view(template_name="monApp/page_home.html"), name="home_no_param"),
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.ContactView.as_view(template_name="monApp/page_home.html"), name="contact"),
    path("aboutus/", views.AboutView.as_view(template_name="monApp/page_home.html"), name="aboutus"),
    path("email-sent/", views.EmailSentView.as_view(), name="email-sent"),

    # PRODUITS
    path("produits/", views.ProduitListView.as_view(), name="lst_prdts"),
    path("produit/<pk>/", views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt_chng"),
    path("produit/<pk>/delete/", views.ProduitDeleteView.as_view(), name="dlt_prdt"),

    # CATEGORIES
    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path("categorie/create/", views.CategorieCreateView.as_view(), name="crt_cat"),
    path("categorie/<pk>/", views.CategorieDetailView.as_view(), name="dtl_cat"),

    # STATUTS
    path("statuts/", views.StatutListView.as_view(), name="lst_status"),
    path("statut/create/", views.StatutCreateView.as_view(), name="crt_statut"),
    path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_statut"),

    # RAYONS
    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/create/", views.RayonCreateView.as_view(), name="crt_rayon"),
    path("rayon/<pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),

    # CATEGORIES CRUD
    path("categorie/<pk>/update/", views.CategorieUpdateView.as_view(), name="upd_cat"),
    path("categorie/<pk>/delete/", views.CategorieDeleteView.as_view(), name="dlt_cat"),

    # STATUTS CRUD
    path("statut/<pk>/update/", views.StatutUpdateView.as_view(), name="upd_statut"),
    path("statut/<pk>/delete/", views.StatutDeleteView.as_view(), name="dlt_statut"),

    # RAYONS CRUD
    path("rayon/<pk>/update/", views.RayonUpdateView.as_view(), name="upd_rayon"),
    path("rayon/<pk>/delete/", views.RayonDeleteView.as_view(), name="dlt_rayon"),

    # CONTENIR ADD
    path('contenir/ajouter/', views.ContenirCreateView.as_view(), name='crt_contenir'),
    path('contenir/<int:pk>/update/', views.UpdateContenirView.as_view(), name='upd_contenir'),
    path('contenir/<int:pk>/delete/', views.DeleteContenirView.as_view(), name='dlt_contenir'),

    path("ma_vue/", views.ma_vue, name="ma_vuuue"),
]
