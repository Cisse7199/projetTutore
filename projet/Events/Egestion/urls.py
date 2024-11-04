from django.urls import path
from . import views

urlpatterns = [
    #path("accueil", views.home),
    path("", views.accueil, name="accueil"),
    path("formconnec", views.form, name="formconnec"),
    path("formevent",views.listEvents, name="formevent"),
    path("paiement",views.paiement, name="paiement"),
    path("aPropos",views.aPropos, name="aPropos"),
    path("pageAide",views.pageAide, name="pageAide"),
    path("listEvenement",views.listEvenement, name="listEvenement"),
    path("form2connec",views.formConnec, name="form2connec"),
    path("monFormTest",views.monFormTest, name="monFormTest"),
    path("formsGoogle",views.formsGoogle, name="formsGoogle")
    
    
]
