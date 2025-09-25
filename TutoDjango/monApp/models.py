from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Hérite déjà de : username, password, email, first_name, last_name, is_active, etc.
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.
class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat
    
class Statut(models.Model):
    idStatut = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    dateFabrication = models.DateField(auto_now=True)
    # Relation CIF : chaque produit appartient à 1 catégorie (0,N côté catégorie 1,1 côté produit)→
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits",null=True, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, related_name="produits",null=True, blank=True)

    def __str__(self):
        return self.intituleProd

class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nomRayon
    
class Contenir(models.Model):
    pk = models.CompositePrimaryKey("refProd", "idRayon", primary_key=True)
    refProd = models.ForeignKey(Produit, on_delete=models.CASCADE)
    idRayon = models.ForeignKey(Rayon, on_delete=models.CASCADE)
    qte = models.IntegerField()
    
    def __str__(self):
        return "Ce produit dans ce rayon possède " + self.qte
