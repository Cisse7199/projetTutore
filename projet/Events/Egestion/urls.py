from django.urls import path
from . import views

urlpatterns = [
    path("accueil", views.home),
    path("", views.accueil, name="accueil"),
    path("<forme>/", views.form, name="form"),
]
