from django.http import HttpResponse, Http404
from django.shortcuts import render
from .forms import monForm
from .models import*;

#Declaration des differents vues pour le client

def home(request):
    """Exemple de page html premier essais"""
    text="""<h1>Bienvenue sur ma page<p>MON SITE DE GESTION EVNTS</P>"""
    #
    return HttpResponse(text)
#Page accueil
def accueil(request):
    return render(request,'Egestion/accueil.html')

#Formulaire de connexion pour devenir membre utilisateur de la page
def form(request):
    return render(request, 'Egestion/form.html')

#Liste des evenements deja creer
def listEvents(request):
    return render(request, 'Egestion/listEvents.html')

#Page de paiement
def paiement(request):
    return render(request, 'Egestion/paiement.html')

#Page aide constitues de FAQ(Questions reponses)
def pageAide(request):
    return render(request, 'Egestion/pageAide.html')

#Pade A propos de l´application et de ses concepteurs(une petite description)
def aPropos(request):
    return render(request, 'Egestion/aPropos.html')

def listEvenement(request):
    return render(request, 'Egestion/listEvenement.html')

def monProfil(request):
    return render(request, 'Egestion/monProfil.html')

def nousJoindre(request):
    return render(request, 'Egestion/nousJoindre.html')

def formConnec(request):
    return render(request, 'Egestion/formConnec.html')

def monFormTest(request):
    form=None
    Nom=""
    if request.method=="POST":
        print("post envoyer")
        form=monForm(request.POST)
        if form.is_valid():
            form.save()
            Nom=form.cleaned_data["Nom"]
            Id_utilisateur=form.cleaned_data["Id_utilisateur"]
            Prenom=form.cleaned_data["Prenom"]
            Email=form.cleaned_data["Email"]
            Password=form.cleaned_data["Password"]
            return render(request,"Egestion/form_test.html")
        else:
            form=monForm()
        return render (request, "Egestion/form_test.html",{"form":form})
    return render (request,"Egestion/form.html",{"form":form})

def formsGoogle(request):
    return render(request, 'Egestion/iframe.html')


    


# Create your views here.
