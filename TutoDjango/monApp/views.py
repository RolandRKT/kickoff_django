from django.shortcuts import render
from django.http import HttpResponse

from .form import ContactUsForm, ProduitForm, CategorieForm, StatutForm, RayonForm
from .models import Produit, Categorie, Statut, Rayon
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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

    def get_queryset(self):
        qs = Produit.objects.select_related('categorie', 'statut').order_by("prixUnitaireProd")
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(intituleProd__icontains=q)
        return qs
    
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
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "Contact us !"
        context['form'] = ContactUsForm()
        return context

    def post(self, request, **kwargs):
        print('La méthode de requête est : ', request.method)
        print('Les données POST sont : ', request.POST)
        if request.method == 'POST':
            form = ContactUsForm(request.POST)
        else:
            form = ContactUsForm()
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monApp.com'],
            )
            return redirect('email-sent')
        return render(
            request,
            self.template_name,
            {
                'titreh1': "Contact us !",
                'form': form
            }
        )
    
class EmailSentView(TemplateView):
    template_name = "monApp/email_sent.html"

# --- CATEGORIE ---
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))

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

    def get_queryset(self):
        return Statut.objects.annotate(nb_produits=Count('produits'))

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

# --- LOGIN ---

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username=username, email=mail, password=password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

# --- PRODUIT ---

@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
    # Jamais utilisée
    def ProduitCreate(request):
        if request.method == 'POST':
            form = ProduitForm(request.POST)
            if form.is_valid():
                prdt = form.save()
                return redirect('dtl_prdt', prdt.refProd)
        else:
            form = ProduitForm()
        return render(request, "monApp/create_produit.html", {'form': form})

@method_decorator(login_required, name='dispatch')
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/update_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

    def ProduitUpdate(request, id):
        prdt = Produit.objects.get(id=id)
        if request.method == 'POST':
            form = ProduitForm(request.POST, instance=prdt)
            if form.is_valid():
                # mettre à jour le produit existant dans la base de données
                form.save()
                # rediriger vers la page détaillée du produit que nous venons de mettre à jour
                return redirect('dtl_prdt', prdt.refProd)
        else:
            form = ProduitForm(instance=prdt)
        return render(request, 'monApp/update_produit.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

# --- CATEGORIE ---
@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"

    def form_valid(self, form):
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"

    def form_valid(self, form):
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cats')

# --- STATUT ---
@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/create_statut.html"

    def form_valid(self, form):
        stat = form.save()
        return redirect('dtl_statut', stat.idStatut)
    
@method_decorator(login_required, name='dispatch')
class StatutUpdateView(UpdateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/update_statut.html"

    def form_valid(self, form):
        stat = form.save()
        return redirect('dtl_statut', stat.idStatut)

@method_decorator(login_required, name='dispatch')
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('lst_status')

# --- RAYON ---
@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"

    def form_valid(self, form):
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"

    def form_valid(self, form):
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')
