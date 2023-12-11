from typing import Any
from django.db import models

class Donnee(models.Model):
    contenu = models.TextField()

    def __str__(self):
        return self.contenu


class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    datePub = models.DateField()
    quantite = models.IntegerField()

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dateNais = models.DateField()
    cycle = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Emprunt(models.Model):
    #Utilisateur, on_delete=models.CASCADE
    #Livre, on_delete=models.CASCADE
    utilisateur = models.CharField(max_length=100)
    livre = models.CharField(max_length=100)
    date_emprunt = models.DateField(max_length=100)
    date_retour = models.DateField(max_length=100)

    def __str__(self):
        return f"{self.utilisateur} emprunte {self.livre}"
