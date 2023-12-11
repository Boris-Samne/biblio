# bibliotheque/forms.py
from django import forms
from .models import Livre, Utilisateur, Emprunt

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'datePub', 'quantite']

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'dateNais', 'cycle','niveau']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['utilisateur', 'livre', 'date_emprunt', 'date_retour']
