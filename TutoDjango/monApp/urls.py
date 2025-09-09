from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # "" = route par défaut
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("produits/", views.ListProduits, name="listproduits"),
]

