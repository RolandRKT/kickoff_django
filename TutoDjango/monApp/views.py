from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut, Rayon
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView

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

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
