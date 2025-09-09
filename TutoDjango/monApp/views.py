from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit
from .models import Categorie
from .models import Statut

# Create your views here.
def home(request, param):
    return HttpResponse(f"<h1>Salut {param}</h1>")

def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1>")

def aboutus(request):
    return HttpResponse("<h1>À propos de nous</h1>")

def ListProduits(request):
    prds = Produit.objects.all()
    lesProduits = "<ul>"
    for p in prds:
        lesProduits = lesProduits + "<li>" + p.intituleProd + "</li>"
    lesProduits = lesProduits + "</ul>"
    return HttpResponse("<h1>Liste des produits</h1>" + lesProduits)

def ListCategories(request):
    pass

def ListStatuts(request):
    pass
    