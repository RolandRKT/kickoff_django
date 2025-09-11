from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit
from .models import Categorie
from .models import Statut

# Create your views here.
def defaultHome(request):
    return HttpResponse("<h1>Bonjour inconnu !</h1>")


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
    cats = Categorie.objects.all()
    lesCats = "<ul>"
    for c in cats:
        lesCats = lesCats + "<li>" + c.nomCat + "</li>"
    lesCats = lesCats + "</ul>"
    return HttpResponse("<h1>Liste des catégories</h1>" + lesCats)

def ListStatuts(request):
    Status = Statut.objects.all()
    lesStatus = "<ul>"
    for s in Status:
        lesStatus = lesStatus + "<li>" + s.libelle + "</li>"
    lesStatus = lesStatus + "</ul>"
    return HttpResponse("<h1>Liste des catégories</h1>" + lesStatus)
    