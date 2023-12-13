from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[  
    path('livres', views.liste_livres, name="livres"),
    path('ajouter_livre', views.newBook, name='ajouter_livre'),
    path('ajouter_etudiant', views.ajouter_etudiant, name="ajouter_etudiant"),
    path('etudiants', views.liste_etudiants, name="etudiants"),
    path('modifier_livres', views.modifier_livres, name="modifier_livres"),
    path('modifier_etudiants', views.modifier_etudiants, name="modifier_etudiants"),
    path('modifier_emprunts', views.modifier_emprunts, name="modifier_emprunts"),
    path('authentification', views.authentification, name='authentification'),
    path('emprunter_livre', views.emprunter_livre, name='emprunter_livre')
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
    document_root= settings.MEDIA_ROOT)