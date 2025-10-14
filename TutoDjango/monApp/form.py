# form.py
from django import forms
from .models import Contenir, Produit, Categorie, Statut, Rayon

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    rayon = forms.ModelChoiceField(queryset=Rayon.objects.all(), required=False)
    class Meta:
        model = Produit
        fields = '__all__'
        exclude = ['id_rayon']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = '__all__'

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = '__all__'

class ContenirForm(forms.ModelForm):
    refProd = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produit")
    idRayon = forms.ModelChoiceField(queryset=Rayon.objects.all(), label="Rayon")
    qte = forms.IntegerField(min_value=1, initial=1, label="Quantité")

    class Meta:
        model = Contenir
        fields = ['refProd', 'idRayon', 'qte']
