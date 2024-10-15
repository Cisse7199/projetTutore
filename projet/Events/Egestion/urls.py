from django.urls import path
from . import views

urlpatterns = [
    #path("accueil", views.home),
    path("", views.accueil, name="accueil"),
    path("formconnec/connexion", views.form, name="formconnec"),
    path("formevent",views.listEvents, name="formevent"),
    path("paiement",views.paiement, name="paiement"),
    path("aPropos",views.aPropos, name="aPropos"),
    path("pageAide",views.pageAide, name="pageAide"),
    path("listEvenement",views.listEvenement, name="listEvenement"),
    path("form2",views.formConnec, name="form2"),
    
]
