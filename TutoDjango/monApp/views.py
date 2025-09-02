from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, param):
    return HttpResponse(f"<h1>Salut {param}</h1>")

def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1>")

def aboutus(request):
    return HttpResponse("<h1>À propos de nous</h1>")