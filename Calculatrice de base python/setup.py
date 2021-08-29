#coding: utf-8
"""ceci est mon programme en ligne de commande de calcul de base"""
#fonction de calcul
Lance = True
def Addition():
    resultat =nbr0 + nbr1
    print("\t {} + {} ={}".format(nbr0,nbr1,resultat))
    """ ceci est ma fonction d'addition

    """
def Soustration():
    resultat = nbr0 - nbr1
    print("{} - {} = {}".format(nbr0,nbr1,resultat))

def Multiplication():
    resultat= nbr0* nbr1
    print("{} * {} = {}".format(nbr0,nbr1,resultat))

def Division():
    resultat= nbr0 / nbr1
    reste = nbr0 % nbr1
    print("\t {}/{} = {} avec {} comme reste.......".format(nbr0,nbr1,resultat,reste)

while Lance:
    saisie_v = input("\t Veillez choisir le type de calcul que vous voulez faire: \n \t 1)-Pour Addition ou Soustration. \n \t 2)-Pour Multiplication ou Division. \n \t -Pour quiter le programme tapez: '5'\n \t" )
    while saisie_v== "1":
        saisie2=input("Veillez à present entre choisir: \n \t 1)-Addition \n \t 2)-Soustraction")
        if saisie2=="1":
            nbr0 = input("\t veiller entrez le premier nombre.:>")
            nbr0=float(nbr0)
            nbr1 = input("\t veillez maintenant entrer le deuxième nombre.:> ")
            nbr1 = float(nbr1)
            Addition()
            saisie_x = input("veiller entrez 5 pour quiter le programme")
            if saisie_x=="5":
                breakpoint
            else :
                saisie_v=="Q" or "q"
        elif saisie2 =="2":
            nbr0 = input("\t veiller entrez le premier nombre.:>")
            nbr0=float(nbr0)
            nbr1 = input("\t veillez maintenant entrer le deuxième nombre.:> ")
            nbr1 = float(nbr1)
            Soustration()
            aisie_x = input("veiller entrez 5 pour quiter le programme")
            if saisie_x=="5":
                breakpoint
            else :
                saisie_v=="Q" or "q"
    while saisie_v=="2":
        saisie2=input("Veillez à present entre choisir: \n \t 1)Multiplication \n \t 2)-Division")
        if saisie2=="1":
            nbr0 = input("\t veiller entrez le premier nombre.:>")
            nbr0=float(nbr0)
            nbr1 = input("\t veillez maintenant entrer le deuxième nombre.:> ")
            nbr1 = float(nbr1)
            Multiplication()
            saisie_x = input("veiller entrez 5 pour quiter le programme")
            if saisie_x=="5":
                breakpoint
            else :
                saisie_v=="Q" or "q"
        elif saisie2 =="2":
            nbr0 = input("\t veiller entrez le premier nombre.:>")
            nbr0=float(nbr0)
            nbr1 = input("\t veillez maintenant entrer le deuxième nombre.:> ")
            nbr1 = float(nbr1)
            Division()
            saisie_x = input("veiller entrez 5 pour quiter le programme")
            if saisie_x=="5":
                breakpoint
            else :
                saisie_v=="Q" or "q"
    while saisie_v == "Q" or "q":
        print("\n \t À Bientot,Merci d'avoir utiliser ce programme chao *_*")
        Lance = False
        break
