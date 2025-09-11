from django.contrib import admin
from .models import Produit
from .models import Categorie
from .models import Statut
from .models import Rayon
from .models import Contenir

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateFabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateFabrication')
    list_filter = ('statut', 'dateFabrication')

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie)
admin.site.register(Statut)
admin.site.register(Rayon)
# admin.site.register(Contenir)

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1 # nombre de lignes vides par défaut

class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]
