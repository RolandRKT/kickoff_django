from django.urls import path
from . import views

urlpatterns = [
    path("", views.defaultHome, name="home"), # "" = route par défaut
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("produits/", views.ListProduits, name="listproduits"),
    path("categories/", views.ListCategories, name="listcategories"),
    path("status/", views.ListStatuts, name="liststatus"),
]

