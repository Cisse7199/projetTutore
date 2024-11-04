from django.contrib import admin


# Register your models here.
from .models import *;
admin.site.register(Paiement)
admin.site.register(utilisateur)
admin.site.register(Evenements)
admin.site.register(billet)


class postadmin(admin.ModelAdmin):
    list_display=("id_utilisateur","Nom","Prenom","Email","password")
