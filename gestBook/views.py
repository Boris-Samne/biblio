# Exemple de lecture du fichier pour les livres
from django.shortcuts import render, redirect
from .forms import LivreForm, UtilisateurForm, EmpruntForm

def lire_livres():
    livres = []
    with open('gestBook/livres.txt', 'r') as f:
        for ligne in f:
            titre, auteur, datePub, quantite = ligne.strip().split('|')
            livre = {'titre': titre, 'auteur': auteur, 'datePub': datePub, 'quantite':quantite}
            livres.append(livre)
    return livres

# Exemple d'écriture dans le fichier pour les livres
def ecrire_livre(livre):
    with open('gestBook/livres.txt', 'a') as f:
        ligne = f"{livre['titre']}|{livre['auteur']}|{livre['quantite']}|{livre['datePub']}\n"
        f.write(ligne)


def livres(request):
    return render(request, "livres.html")

def newBook(request):
    return render(request, "newBook.html")

def liste_livres(request):
    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')
    return render(request, 'livres.html', {'livres': livres})

def lire_livres_depuis_fichier_texte(chemin_fichier):
    livres = []
    try:
        with open(chemin_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                titre, auteur, datePub, quantite = ligne.strip().split('|')
                livre = {
                    'titre': titre,
                    'auteur': auteur,
                    'datePub': datePub,
                    'quantite': quantite
                }
                livres.append(livre)
    except FileNotFoundError:
        # Gérer l'absence du fichier
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        # Gérer d'autres erreurs éventuelles
        print(f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
    
    return livres

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            datePub = form.cleaned_data['datePub']
            quantite = form.cleaned_data['quantite']

            # Création d'une chaîne de données pour le livre
            livre_data = f"{titre}|{auteur}|{datePub}|{quantite}\n"

            # Enregistrement dans le fichier texte
            try:
                with open('gestBook/livres.txt', 'a') as fichier:
                    fichier.write(livre_data)
            except Exception as e:
                # Gérer d'éventuelles erreurs d'écriture dans le fichier
                print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

            return redirect('livres')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = LivreForm()

    return render(request, 'bibliotheque/ajouter_livre.html', {'form': form})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            dateNais = form.cleaned_data['dateNais']
            cycle = form.cleaned_data['cycle']
            niveau = form.cleaned_data['niveau']

            # Création d'une chaîne de données pour l'étudiant'
            student_data = f"{nom}|{prenom}|{dateNais}|{cycle}|{niveau}\n"

            # Enregistrement dans le fichier texte
            try:
                with open('gestBook/etudiants.txt', 'a') as fichier:
                    fichier.write(student_data)
            except Exception as e:
                # Gérer d'éventuelles erreurs d'écriture dans le fichier
                print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

            return redirect('etudiants')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = UtilisateurForm()

    return render(request, 'newStudent.html', {'form': form})

def liste_etudiants(request):
    etudiants = lire_etudiants_depuis_fichier_texte('gestBook/etudiants.txt')
    return render(request, 'etudiants.html', {'etudiants': etudiants})

def lire_etudiants_depuis_fichier_texte(chemin_fichier):
    etudiants = []
    try:
        with open(chemin_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                nom, prenom, dateNais, cycle, niveau = ligne.strip().split('|')
                etudiant = {
                    'nom': nom,
                    'prenom': prenom,
                    'dateNais': dateNais,
                    'cycle': cycle,
                    'niveau':niveau
                }
                etudiants.append(etudiant)
    except FileNotFoundError:
        # Gérer l'absence du fichier
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        # Gérer d'autres erreurs éventuelles
        print(f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
    
    return etudiants

def newstudent(request):
    return render(request, "newstudent.html")


def modifier_livres(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            datePub = form.cleaned_data['datePub']
            quantite = form.cleaned_data['quantite']
            redirect('livres')
            print("Titres:", titre)
            print("Auteurs:", auteur)
            print("Dates de Publication:", datePub)
            print("Quantités:", quantite)


            # Créer une liste de chaînes de données pour chaque livre
            livres_data = [f"{titr}|{auteu}|{datePu}|{quantit}" for titr, auteu, datePu, quantit in zip(titre, auteur, datePub, quantite)]

            # Enregistrement dans le fichier texte
            try:
                with open('gestBook/livres.txt', 'w') as fichier:
                    fichier.write('\n'.join(livres_data) + '\n')
            except Exception as e:
                # Gérer d'éventuelles erreurs d'écriture dans le fichier
                print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

            return redirect('livres')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = LivreForm()

    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')
    return render(request, 'modifier_livres.html', {'form': form, 'livres':livres})

def emprunter_livre(request):
    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')

    if request.method == 'POST':
        livre_id = request.POST.get('livre_id')
        # Ajoutez ici la logique pour traiter l'emprunt (par exemple, enregistrer dans un fichier texte)
        ecrire_emprunt(livre_id)

        return redirect('livres')  # Rediriger vers la liste des livres après l'emprunt

    return render(request, 'emprunter_livre.html', {'livres': livres})

def ecrire_emprunt(livre_id):
    # Ajoutez ici la logique pour enregistrer l'emprunt dans un fichier texte
    with open('gestBook/emprunts.txt', 'a') as fichier:
        fichier.write(f"{livre_id}\n")