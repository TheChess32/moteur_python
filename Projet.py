import tkinter as tk
import csv
from random import *

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

createAccount("test", "Bonsoir")
vers_csv("accounts", ["Pseudo", "Mot de passe", "Chiffre de cryptage"])