from django.urls import path
from . import views

urlpatterns=[  
    path('livres', views.liste_livres, name="livres"),
    path('newBook', views.newBook, name="nouveau"),
    path('ajouter_livre/', views.ajouter_livre, name='ajouter_livre'),
    path('ajouter_etudiant', views.ajouter_etudiant, name="ajouter_etudiant"),
    path('etudiants', views.liste_etudiants, name="etudiants"),
    path('modifier_livres', views.modifier_livres, name="modifier_livres"),
    path('emprunter_livre/', views.emprunter_livre, name='emprunter_livre')
]