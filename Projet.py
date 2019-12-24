import tkinter as tk
import csv
import random as rdm

connected = False
pseudo_connected = ""

def depuis_csv(fichier):
    try:
        fichier1=open(fichier + '.csv','r',encoding='utf-8')
        lecteur = csv.DictReader(fichier1,delimiter=',')
        return [dict(ligne) for ligne in lecteur]
    except:
        vers_csv("Accounts", ["Pseudo", "Mot de passe", "Chiffre de cryptage"])
        fichier1=open(fichier + '.csv','r',encoding='utf-8')
        lecteur = csv.DictReader(fichier1,delimiter=',')
        return [dict(ligne) for ligne in lecteur]

def vers_csv(nom, ordre):
    try:
        fic=open(nom + '.csv', 'w',encoding='utf-8')
        ecrit= csv.DictWriter(fic,fieldnames=ordre)
        ecrit.writeheader()
        table = eval(nom)
        for ligne in table:
            ecrit.writerow(ligne)
    except:
        fic=open(nom + '.csv', 'w',encoding='utf-8')
        ecrit= csv.DictWriter(fic,fieldnames=ordre)
        ecrit.writeheader()

accounts = depuis_csv("Accounts")

def verifPassword(pseudo, mdp):
    global accounts
    if accountExists(pseudo):
        for account in accounts:
            if account["Pseudo"] == pseudo:
                mdp_crypte = account["Mot de passe"]
                chiffre_de_cryptage = int(account["Chiffre de cryptage"])
                if str(cryptagePassword(mdp, chiffre_de_cryptage)) == mdp_crypte:
                    return True
                else:
                    return False

def cryptagePassword(mdp, chiffre_de_cryptage):
    mdp_crypte=[]
    for car in mdp:
        mdp_crypte.append(ord(car)+chiffre_de_cryptage)
    return mdp_crypte

def accountExists(pseudo):
    global accounts
    for account in accounts:
        if account["Pseudo"] == pseudo:
            return True
    return False

def createAccount(pseudo, mdp):
    global accounts
    global connected
    global pseudo_connected
    new_donnees = {}
    chiffre_de_cryptage = rdm.randint(5,100)
    cryptage = cryptagePassword(mdp, chiffre_de_cryptage)
    mdp = cryptage
    if accountExists(pseudo):
        print(f"{pseudo} est déjà utilisé !")
    else: 
        new_donnees["Pseudo"] = pseudo
        new_donnees["Mot de passe"] = str(mdp)
        new_donnees["Chiffre de cryptage"] = chiffre_de_cryptage
        accounts.append(new_donnees)
        connected = True
        pseudo_connected = pseudo       
        vers_csv("accounts", ["Pseudo", "Mot de passe", "Chiffre de cryptage"])
        print(f"Votre compte a été créé avec succès ! Vous êtes désormais connecté avec le pseudo : {pseudo_connected}")
        

def create_menu(accueil):
    global pseudo_connected
    menu_bar = tk.Menu(accueil)
    
    def pre_accueil_connexion(accueil = accueil):
        return accueil_connexion(accueil)
    
    def pre_accueil_creation(accueil = accueil):
        return accueil_creation(accueil)
    
    def pre_choix_jeu(accueil = accueil):
        return choix_jeu(accueil)
    
    def pre_disconnect(pseudo = pseudo_connected, accueil = accueil):
        return disconnect(pseudo, accueil)
    
    if connected:     
        profil = tk.Menu(menu_bar, tearoff = 0)
        profil.add_command(label = f"Vous êtes connecté avec le pseudo : {pseudo_connected}")
        profil.add_command(label = "Se déconnecter", command=pre_disconnect)
        menu_bar.add_cascade(label = "Mon profil", menu = profil)
        
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label = "Fermer", command=accueil.destroy)
    
    choisir_jeu = tk.Menu(menu_bar, tearoff=0)
    choisir_jeu.add_command(label = "Jouer à un jeu", command=pre_choix_jeu)
    
    connexion = tk.Menu(menu_bar, tearoff=0)
    connexion.add_command(label = "Se connecter", command=pre_accueil_connexion)
    connexion.add_command(label = "Créer un compte", command=pre_accueil_creation)
    
    menu_bar.add_cascade(label="Menu", menu=file_menu)
    menu_bar.add_cascade(label="Connexion", menu=connexion)
    menu_bar.add_cascade(label="Jeux", menu=choisir_jeu)
    
    accueil.config(menu=menu_bar)

def accueil_connexion(accueil):
    for widget in accueil.winfo_children():
        widget.destroy()
    
    create_menu(accueil)
    frame = tk.Frame(accueil, bg = "#0B5A6F")
    right_frame = tk.Frame(frame, bg = "#0B5A6F")
    
    if connected:
        choix_jeu(accueil)
    else:
        titre_seconnecter = tk.Label(right_frame, text = "Se connecter :", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_seconnecter.pack()
        titre_vide = tk.Label(right_frame, text = "", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_vide.pack()
        
        titre_pseudo = tk.Label(right_frame, text = "Entrez votre pseudo :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_pseudo.pack()
        entree_pseudo=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center", bd=0)
        entree_pseudo.pack()
        
        titre_mdp = tk.Label(right_frame, text = "Entrez votre mot de passe :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_mdp.pack()
        entree_mdp=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center", show="●", bd=0)
        entree_mdp.pack()
        
        bouton_confirmer = tk.Button(right_frame, text = "Valider", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center", relief="raised")
        bouton_confirmer.pack()
        
        titre_vide3 = tk.Label(right_frame, text = "", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_vide3.pack()
        bouton_creer_compte = tk.Button(right_frame, text="Créer un compte",bg="#0B5A6F",font=("Helvetica",10),fg="white",justify="center",bd=0,activebackground = "#0B5A6F",activeforeground="#2B7589")
        bouton_creer_compte.pack()
        
        def pre_connect(event, pseudo_=entree_pseudo, mdp_=entree_mdp, frame=frame, accueil=accueil):
            pseudo_.update()
            pseudo = pseudo_.get()
            mdp_.update()
            mdp = mdp_.get()
            return connect(event, pseudo, mdp, frame, accueil)
        
        def pre_accueil_creation(event, accueil = accueil):
            return accueil_creation(accueil)
        
        bouton_confirmer.bind("<1>", pre_connect)
        bouton_creer_compte.bind("<1>", pre_accueil_creation)
        
        right_frame.grid(row=0, column = 1, sticky=tk.W)
        frame.pack(expand=tk.YES)

def choix_jeu(accueil):
    for widget in accueil.winfo_children():
        widget.destroy()
        
    create_menu(accueil)
    frame = tk.Frame(accueil, bg = "#0B5A6F")    
    right_frame = tk.Frame(frame, bg = "#0B5A6F")
    if connected:
        titre = tk.Label(right_frame, text = "Choisissez un jeu :", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre.pack()
        
    else:
        titre = tk.Label(right_frame, text = "Vous n'êtes pas connecté :/", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre.pack()
        titre = tk.Label(right_frame, text = "", bg="#0B5A6F", font=("Helvetica",25), fg="white", justify = "center")
        titre.pack()
        
        bouton_creer_compte = tk.Button(right_frame, text="Créer un compte",bg="#0B5A6F",font=("Helvetica",25),fg="white",justify="center",bd=0,activebackground = "#0B5A6F",activeforeground="#2B7589")
        bouton_creer_compte.pack()
        
        bouton_se_connecter = tk.Button(right_frame, text="Se connecter",bg="#0B5A6F",font=("Helvetica",25),fg="white",justify="center",bd=0,activebackground = "#0B5A6F",activeforeground="#2B7589")
        bouton_se_connecter.pack()
        
        def pre_accueil_creation(event, accueil = accueil):
            return accueil_creation(accueil)
        
        def pre_accueil_connexion(event, accueil = accueil):
            return accueil_connexion(accueil)
        
        bouton_se_connecter.bind("<1>", pre_accueil_connexion)
        bouton_creer_compte.bind("<1>", pre_accueil_creation)
        
    right_frame.grid(row=0, column = 1, sticky=tk.W)
    frame.pack(expand=tk.YES)

def accueil_creation(accueil):
    for widget in accueil.winfo_children():
        widget.destroy()
    
    if connected:
        choix_jeu(accueil)
    else:
        create_menu(accueil)
        
        frame = tk.Frame(accueil, bg = "#0B5A6F")    
        right_frame = tk.Frame(frame, bg = "#0B5A6F")
        
        titre_creation = tk.Label(right_frame, text = "Créer un compte :", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_creation.pack()
        titre_vide = tk.Label(right_frame, text = "", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_vide.pack()
        
        titre_pseudo = tk.Label(right_frame, text = "Entrez votre pseudo :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_pseudo.pack()
        entree_pseudo=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center", bd=0)
        entree_pseudo.pack()
        
        titre_mdp = tk.Label(right_frame, text = "Entrez votre mot de passe :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_mdp.pack()
        entree_mdp=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center", show="●", bd=0)
        entree_mdp.pack()
        
        bouton_confirmer = tk.Button(right_frame, text = "Valider", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center", relief="raised")
        bouton_confirmer.pack()
        
        right_frame.grid(row=0, column = 1, sticky=tk.W)
        frame.pack(expand=tk.YES)

def accueil():
    # Création de la fenêtre
    accueil = tk.Tk()
    accueil.title("Accueil")
    accueil.geometry("1080x720")
    accueil.minsize(540, 360)
    accueil.maxsize(1080, 720)
    accueil.iconbitmap("logo.ico")
    accueil.config(background = "#0B5A6F")
    accueil_connexion(accueil)
    
    create_menu(accueil)
    
    accueil.mainloop()

def connect(event, pseudo, mdp, frame, accueil):
    global connected
    global pseudo_connected
    if verifPassword(pseudo, mdp):
        connected = True
        pseudo_connected = pseudo
        print(f"Vous avez été connecté avec le pseudo {pseudo_connected} avec succès !")
        frame.destroy()
        choix_jeu(accueil)
    else:
        print("false")

def disconnect(pseudo, accueil):
    global connected
    global pseudo_connected
    pseudo_connected = ""
    connected = False
    accueil_connexion(accueil)
        
accueil()
vers_csv("accounts", ["Pseudo", "Mot de passe", "Chiffre de cryptage"])
