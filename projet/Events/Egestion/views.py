from django.http import HttpResponse, Http404
from django.shortcuts import render

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
def form(request, forme:str):
    return render(request, 'Egestion/form.html')

#Liste des evenements deja creer
def listEvents(request):
    return render(request, 'Egestion/listEvents.html')

#Page de paiement
def paiement(request):
    return render(request, 'Egestion/paiement.html')

#Page aide constitues de FAQ(Questions reponses)
def pageAideI(request):
    return(request, 'Egestion/pageAide.html')

#Pade A propos de l´application et de ses concepteurs(une petite description)
def aPropos(request):
    return(request, 'Egestion/aPropos.html')
    


# Create your views here.
