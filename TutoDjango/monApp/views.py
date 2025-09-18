from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut, Rayon
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.

def home(request,param=None):

    if request.GET and request.GET["test"]:
        raise Http404
    
    if param is None:
        print(dir(request))
        print(request.__dict__)
        string = request.GET['name']
        return HttpResponse("Bonjour %s!" % string)
    else:
        return HttpResponse(f"<h1>Hello {param} !</h1>")
    
def about(request):
    return HttpResponse("<p> Bienvenu sur la page A propos !</p>")
    
def contact(request):
    return HttpResponse("<p> Bienvenu sur la page de contact !</p>")

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})

def ListStatuts(request):
    Status = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'status': Status})

def ListRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})

