from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.about, name="aboutus"),
    path("produits/", views.ListProduits, name="listproduits"),
    path("categories/", views.ListCategories, name="listcategories"),
    path("status/", views.ListStatuts, name="liststatus"),
    path('ma_vue/', views.ma_vue, name="ma_vuuue")
]

