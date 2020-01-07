import csv
def depuis_csv(fichier):
    # fichier est au format csv et doit avoir été bien encodé en utf8.
    fichier1=open(fichier + '.csv','r',encoding='utf-8')
    # 'r' siginifie read, On ouvre fichier en mode lecture,
    lecteur = csv.DictReader(fichier1,delimiter=',')
    # la fonction DictReader de csv prend en argument un fichier ouvert.
    return [dict(ligne) for ligne in lecteur]

def valide(x):
    # prend un dictionnaire en entrée
    prenom = x["prénom"]
    jour = int(x["jour"])
    mois = int(x["mois"])
    annee = int(x["année"])
    projet = x["projet"] # On n'a rien modifié pour les champs prenom et projet : on garde des strings.
    return{"prénom":prenom,"jour":jour,"mois":mois,"année":annee,"projet": projet}

def verif_type(table):
    Exceptions = []
    print(table[0])
    for x in tabl:
        for cle in list(table[0].keys()):
            if type(x[cle]) != type(table[0] [cle]):
                Exceptions.append(x)
                table.remove(x)
                break
    print("Table :", table)
    print("Exceptions :", Exceptions)
    return table, Exceptions

tabl=depuis_csv('eleves')
tabl = [valide(dicto) for dicto in tabl]
print(tabl)

def vers_csv (nom, ordre):
    # nom = le nom de la table est donné sous forme de string.
    # ordre est la liste des attributs (des champs) de la table nom.
    # on pourrait supprimer ce paramètre car il est ('très souvent') égal à list(eval(nom)[0]).
    fic=open('nouveau_'+nom + '.csv', 'w',encoding='utf-8')
    # on ouvre un fichier en écriture, c'est ce qui est indiqué par le paramètre 'w' (write) passé à open.
    # Si le fichier nouveau_nom.csv n'existait pas, il est alors créé. S'il existait, il est écrasé.
    ecrit= csv.DictWriter(fic,fieldnames=ordre)
    # On appelle la fonction DictWriter en lui passant le fichier qu'on vient d'ouvrir
    # en écriture et la liste des attributs de la table (fieldnames signifie noms de champs).
    #L'objet ecrit créé va permettre d'écrire des lignes dans le fichier.
    ecrit.writeheader()
    # écrit la première ligne, celle des attributs.
    table = eval(nom) # sinon nom est une string.
    for ligne in table:
        ecrit.writerow(ligne)
    # ajoute les lignes de la table

vers_csv('tabl',list(tabl[0]))

def liste_de_projet_de(pren,eleves) :
    L=[]
    for e in eleves :
        if e['prénom']==pren:
            L.append(e['projet'])
    return L

print("\n", liste_de_projet_de('Alan',tabl), "\n")

def recherche_valeur1(cle1, cle2, valeur2, table):
    L = []
    for e in table:
        if e[cle2] == valeur2:
            L.append(e[cle1])
    return L

print(recherche_valeur1("prénom", "mois", 1, tabl))

tab2=[{'prénom':e['prénom'],'projet' :e['projet']} for e in tabl if e['projet'].find("programme") != -1]
print("\n", tab2)