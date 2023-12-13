# Exemple de lecture du fichier pour les livres
from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
from .forms import LivreForm, UtilisateurForm
from django.utils import timezone

def authentification(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)

        if  username== "Admin" and password=="1234":
            #login(request, user)
            # Redirigez l'utilisateur vers la page d'accueil ou une autre page après l'authentification réussie.
            return redirect('emprunter_livre')
        else:
            # Gérez le cas où l'authentification échoue (par exemple, affichez un message d'erreur).
            pass

    return render(request, 'authentification.html')
def lire_livres():
    livres = []
    with open('gestBook/livres.txt', 'r') as f:
        for ligne in f:
            titre, auteur, datePub, quantite = ligne.strip().split('|')
            livre = {'titre': titre, 'auteur': auteur, 'datePub': datePub, 'quantite':quantite}
            livres.append(livre)
    return livres

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
    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')
    livres_data = []

    if request.method == 'POST':
        for i,livre in enumerate(livres):
            # Récupérer les données du formulaire
            titre = request.POST.get(f"titre{ i }")
            auteur = request.POST.get(f"auteur{ i }")
            datePub = request.POST.get(f"datePub{ i }")
            quantite = request.POST.get(f"quantite{ i }")
            print(f"titre{ i }")
            # Assurez-vous que les champs ne sont pas nuls avant de les ajouter à livres_data
            if titre or auteur or datePub or quantite:
                livres_data.append(f"{titre}|{auteur}|{datePub}|{quantite}\n")
            else:
                print('données vides')

        # Enregistrement dans le fichier texte
        try:
            with open('gestBook/livres.txt', 'w') as fichier:
                fichier.writelines(livres_data)
        except Exception as e:
            # Gérer d'éventuelles erreurs d'écriture dans le fichier
            print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

        return redirect('livres')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = LivreForm()

    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')
    livres= enumerate(livres)
    return render(request, 'modifier_livres.html', {'form': form, 'livres': livres})

def modifier_etudiants(request):
    etudiants = lire_etudiants_depuis_fichier_texte('gestBook/etudiants.txt')
    etudiants_data = []

    if request.method == 'POST':
        for i,etudiants in enumerate(etudiants):
            # Récupérer les données du formulaire
            nom = request.POST.get(f"nom{ i }")
            prenom = request.POST.get(f"prenom{ i }")
            dateNais = request.POST.get(f"dateNais{ i }")
            cycle = request.POST.get(f"cycle{ i }")
            niveau=request.POST.get(f"niveau{ i }")

            print(f"titre{ i }")
            # Assurez-vous que les champs ne sont pas nuls avant de les ajouter à livres_data
            if nom or prenom or dateNais or cycle or niveau:
                etudiants_data.append(f"{nom}|{prenom}|{dateNais}|{cycle}|{niveau}\n")
            else:
                print('données vides')

        # Enregistrement dans le fichier texte
        try:
            with open('gestBook/etudiants.txt', 'w') as fichier:
                fichier.writelines(etudiants_data)
        except Exception as e:
            # Gérer d'éventuelles erreurs d'écriture dans le fichier
            print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

        return redirect('etudiants')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = UtilisateurForm()

    etudiants = lire_etudiants_depuis_fichier_texte('gestBook/etudiants.txt')
    etudiants= enumerate(etudiants)
    return render(request, 'modifier_etudiants.html', {'form': form, 'etudiants': etudiants})

def lire_emprunts_depuis_fichier_texte(chemin_fichier):
    emprunts = []
    try:
        with open(chemin_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                titre, nomprenom, dateEmp, dateRet = ligne.strip().split('|')
                emprunt = {
                    'titre': titre,
                    'nomprenom': nomprenom,
                    'dateEmp': dateEmp,
                    'dateRet': dateRet
                }
                emprunts.append(emprunt)
    except FileNotFoundError:
        # Gérer l'absence du fichier
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        # Gérer d'autres erreurs éventuelles
        print(f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
    
    return emprunts

def modifier_emprunts(request):
    emprunts = lire_emprunts_depuis_fichier_texte('gestBook/emprunts.txt')
    emprunts_data = []

    if request.method == 'POST':
        for i,emprunt in enumerate(emprunts):
            # Récupérer les données du formulaire
            titre = request.POST.get(f"titre{ i }")
            nomprenom = request.POST.get(f"nomprenom{ i }")
            dateEmp = request.POST.get(f"dateEmp{ i }")
            dateRet = request.POST.get(f"dateRet{ i }")

            print(f"titre{ i }")
            # Assurez-vous que les champs ne sont pas nuls avant de les ajouter à livres_data
            if bool(titre) and bool(nomprenom) and bool(dateEmp) and bool(dateRet) :
                emprunts_data.append(f"{titre}|{nomprenom}|{dateEmp}|{dateRet}\n")
            else:
                print('données vides')
                continue

        # Enregistrement dans le fichier texte
        try:
            with open('gestBook/emprunts.txt', 'w') as fichier:
                fichier.writelines(emprunts_data)
        except Exception as e:
            # Gérer d'éventuelles erreurs d'écriture dans le fichier
            print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")

        return redirect('modifier_emprunts')  # Rediriger vers la liste des livres après l'enregistrement

    else:
        form = UtilisateurForm()

    emprunts = lire_emprunts_depuis_fichier_texte('gestBook/emprunts.txt')
    emprunts= enumerate(emprunts)
    return render(request, 'modifier_emprunts.html', {'form': form, 'emprunts': emprunts})

def emprunter_livre(request):
    # Récupérer la liste des livres et des étudiants depuis la base de données
    livres = lire_livres_depuis_fichier_texte('gestBook/livres.txt')
    etudiants = lire_etudiants_depuis_fichier_texte('gestBook/etudiants.txt')


    if request.method == 'POST':
        # Récupérer les données du formulaire
        titre = request.POST['livre']
        nomprenom = request.POST['etudiant']
        # Récupérer les instances du livre et de l'étudiant

        date_emprunt = timezone.now()
        date_empf = date_emprunt.strftime('%Y-%m-%d')
        date_e = date_emprunt + timezone.timedelta(days=14)  # 2 semaines à partir de la date d'emprunt
        date_retf= date_e.strftime('%Y-%m-%d')

        #emprunt ={"livre": livre["titre"], "etudiant":nomprenom, "date_emprunt":date_emprunt, "date_retour":date_retour}
        if titre and nomprenom and date_emprunt and date_retf:
            emprunt_data = f"{titre}|{nomprenom}|{date_empf}|{date_retf}\n"
        # Enregistrer l'emprunt dans le fichier texte
            enregistrer_emprunt_dans_fichier(emprunt_data)

        return redirect('livres')  # Rediriger vers la liste des emprunts après l'enregistrement

    # Passer les listes des livres et des étudiants au template
    context = {'livres': livres, 'etudiants': etudiants}
    return render(request, 'emprunter_livre.html', context)

def enregistrer_emprunt_dans_fichier(emprunt):
    # Enregistrement dans le fichier texte
    with open('gestBook/emprunts.txt', 'a') as fichier_emprunts:
        fichier_emprunts.write(emprunt)