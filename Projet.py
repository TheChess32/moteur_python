import tkinter as tk
import csv
from random import *

connected = False
test = "aa"

def depuis_csv(fichier):
    fichier1=open(fichier + '.csv','r',encoding='utf-8')
    lecteur = csv.DictReader(fichier1,delimiter=',')
    return [dict(ligne) for ligne in lecteur]

def vers_csv(nom, ordre):
    fic=open(nom + '.csv', 'w',encoding='utf-8')
    ecrit= csv.DictWriter(fic,fieldnames=ordre)
    ecrit.writeheader()
    table = eval(nom)
    for ligne in table:
        ecrit.writerow(ligne)

accounts = depuis_csv("Accounts")

def verifPassword(pseudo, mdp):
    global accounts
    if accountExists(pseudo):
        for account in accounts:
            if account["Pseudo"] == pseudo:
                mdp_crypte = account["Mot de passe"]
                chiffre_de_cryptage = int(account["Chiffre de cryptage"])
                print (cryptagePassword(mdp, chiffre_de_cryptage))
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
    new_donnees = {}
    chiffre_de_cryptage = randint(5,100)
    cryptage = cryptagePassword(mdp, chiffre_de_cryptage)
    mdp = cryptage
    if accountExists(pseudo):
        print(f"{pseudo} est déjà utilisé !")
    else: 
        new_donnees["Pseudo"] = pseudo
        new_donnees["Mot de passe"] = str(mdp)
        new_donnees["Chiffre de cryptage"] = chiffre_de_cryptage
        accounts.append(new_donnees)

def accueil():
    # Création de la fenêtre
    accueil = tk.Tk()
    accueil.title("Accueil")
    accueil.geometry("1080x720")
    accueil.minsize(540, 360)
    accueil.maxsize(1080, 720)
    accueil.iconbitmap("logo.ico")
    accueil.config(background = "#0B5A6F")
                   
    #fenetre = tk.Canvas(accueil, bg="#0EABB8")
    #fenetre.pack()

    menu_bar = tk.Menu(accueil)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label = "Fermer", command=accueil.destroy)
    menu_bar.add_cascade(label="Menu", menu=file_menu)
    
    frame = tk.Frame(accueil, bg = "#0B5A6F")
    right_frame = tk.Frame(frame, bg = "#0B5A6F")
    
    if connected:
        print("")
    else:
        titre_seconnecter = tk.Label(right_frame, text = "Se connecter :", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_seconnecter.pack()
        titre_vide = tk.Label(right_frame, text = "", bg="#0B5A6F", font=("Helvetica",50), fg="white", justify = "center")
        titre_vide.pack()
        
        titre_pseudo = tk.Label(right_frame, text = "Entrez votre pseudo :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_pseudo.pack()
        entree_pseudo=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center")
        entree_pseudo.pack()
        
        titre_mdp = tk.Label(right_frame, text = "Entrez votre mot de passe :", bg="#0B5A6F", font=("Helvetica",20), fg="white", justify = "center")
        titre_mdp.pack()
        entree_mdp=tk.Entry(right_frame, bg="#2B7589", font=("Helvetica",20), fg="white", justify = "center", show="*")
        entree_mdp.pack()
        
        def pre_connect(event, entree=entree_pseudo):
            entree.update()
            pseudo = entree.get()
            return connect(event, pseudo)
            
        accueil.bind("<Return>", pre_connect)
        
        right_frame.grid(row=0, column = 1, sticky=tk.W)
        frame.pack(expand=tk.YES)
    
    accueil.config(menu=menu_bar)
    
    accueil.mainloop()


def connect(event, mdp):
    global connected
    print(mdp)
    connected = True

accueil()
vers_csv("accounts", ["Pseudo", "Mot de passe", "Chiffre de cryptage"])