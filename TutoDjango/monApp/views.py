from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut, Rayon
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView

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

def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})

def ListStatuts(request):
    Status = Statut.objects.all()
    return render(request, 'monApp/list_statut.html',{'status': Status})

def ListRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    queryset = Produit.objects.filter(refProd=2)

    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class ContactView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Mon contact..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
# --- CATEGORIE ---
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Liste des catégories"
        return context


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Détail de la catégorie"
        return context


# --- STATUT ---
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statut.html"
    context_object_name = "status"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Liste des statuts"
        return context


class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "statut"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Détail du statut"
        return context


# --- RAYON ---
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Liste des rayons"
        return context


class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titremenu"] = "Détail du rayon"
        return context
