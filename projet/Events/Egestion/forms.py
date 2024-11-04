
from django import forms;

class monForm(forms.Form):
    Id_utilisateur=forms.CharField(label="Identifiant d´utilisateur", max_length=50);
    Nom=forms.CharField(label="Nom", max_length=50)
    Prenom=forms.CharField(label="Prenom", max_length=50)
    Email=forms.EmailField(label="Votre e-mail", max_length=50)
    Password=forms.CharField(label="Mot de passe", max_length=50)
    
class monEvent(forms.Form):
    Id_evenement=forms.CharField(label="Identifiant de l evenement", max_length=30)
    Type_evenement=forms.CharField(label="Type de l evenement", max_length=50)
    Id_utilisateur=forms.CharField(label="Identifiant de l´utilisateur", max_length=30)
    Date_creation=forms.DateField(label="Date de creation ")
    Description_evenement=forms.CharField(label="Description de l´evenement", max_length=250)
    nom_user=forms.CharField(label="Votre nom", max_length=30)
    prenom_user=forms.CharField(label="Votre prenom", max_length=30)
    email_user=forms.EmailField(label="Votre e-mail", max_length=50)
    
    
    