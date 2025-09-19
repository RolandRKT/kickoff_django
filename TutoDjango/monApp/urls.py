from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(template_name="monApp/page_home.html")),
    path("home/<param>/", views.home, name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("aboutus/", views.AboutView.as_view(), name="aboutus"),
    path("produits/", views.ListProduits, name="listproduits"),
    path("categories/", views.ListCategories, name="listcategories"),
    path("status/", views.ListStatuts, name="liststatus"),
    path("rayons/", views.ListRayons, name="listrayons"),
    path('ma_vue/', views.ma_vue, name="ma_vuuue"),
]
