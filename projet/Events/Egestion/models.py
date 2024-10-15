from django.db import models

# Create your models here.
class Paiement(models.Model):
    id_paiement=models.CharField(max_length=50)
    Nom_utilisateur=models.CharField(max_length=30)
    id_evenement=models.CharField(max_length=30)
    Date_paiement=models.DateField(max_length=30)


class utilisateur(models.Model):
    id_utilisateur=models.CharField(max_length=30)
    Nom=models.CharField(max_length=30)
    Prenom=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    
    
class Evenements(models.Model):
    Id_evenement=models.IntegerField(max_length=30)
    Id_utilisateur=models.IntegerField(max_length=30)
    Type_evenement=models.CharField(max_length=30)
    Date_creation=models.DateTimeField(auto_now_add=True)
    Description_evenement=models.CharField(max_length=200)
    Nom_user=models.CharField(max_length=30)
    Emal_user=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    
    
class billet(models.Model):
    id_billet=models.CharField(max_length=30)
    Type_billet=models.CharField(max_length=30)
    Id_utilisateur=models.CharField(max_length=30)
    Id_evenement=models.CharField(max_length=30)
    
    
    
    

    