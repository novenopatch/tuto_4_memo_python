def Addition():
    nbr0 = input("\tVeillez saisir le premier nombre du calcul:>")
    nbr1 = input("Veilllez maintenant entrez le deuxième nombre du calcul:>")
    nbr0=float(nbr0)
    nbr1=float(nbr1)
    resultat =nbr0 + nbr1
    print("\t {} + {} ={}".format(nbr0,nbr1,resultat))
def Soustration():
    nbr0 = input("\tVeillez saisir le premier nombre du calcul:>")
    nbr1 = input("Veilllez maintenant entrez le deuxième nombre du calcul:>")
    nbr0=float(nbr0)
    nbr1=float(nbr1)
    resultat = nbr0 - nbr1
    print("{} - {} = {}".format(nbr0,nbr1,resultat))

def Multiplication():
    nbr0 = input("\tVeillez saisir le premier nombre du calcul:>")
    nbr1 = input("Veilllez maintenant entrez le deuxième nombre du calcul:>")
    nbr0=float(nbr0)
    nbr1=float(nbr1)
    resultat= nbr0* nbr1
    print("{} * {} = {}".format(nbr0,nbr1,resultat))

def Division():
    nbr0 = input("\tVeillez saisir le premier nombre du calcul:>")
    nbr1 = input("Veilllez maintenant entrez le deuxième nombre du calcul:>")
    nbr0=float(nbr0)
    nbr1=float(nbr1)
    resultat= nbr0 / nbr1
    reste = nbr0 % nbr1
    print("\t {}/{} = {} avec {} comme reste.......".format(nbr0,nbr1,resultat,reste))
programme_variable = True

if programme_variable == True:
    print("\n \t \t BIENVENUE DANS LE PROGRAMME DE CALCUL")
    saisie_s = input("\n \t \t Veillez entrer la lettre correspondans au type de calcul que vous voulez faire. \n \t \t 1)-POUR Addition et Soustraction entrez(1).:> \n \t \t 2)-POUR Mutiplication et Division(2).:> \n \t \t 3)-Pour quiter le programme entre(3).   :>")
    while saisie_s =="1":
        saisie_s1 = input("\t \t ADDITION et SOUSTRATION \n \t \t Veillez maintenant choisir \n \t \t \t1)-ADDITION:> \n \t \t \t2)-SOUSTRATION")
        if saisie_s1 == "1":
            Addition()
        elif saisie_s1=="2":
            Soustration()
        if saisie_s1 == "3":
            breakpoint
        if saisie_s1 =="5":
            programme_variable= False
            break
    while saisie_s=="2":
        saisie_s1 = input("\t \t MULTIPLICATION et DIVISION \n \t \t Veillez maintenant choisir \n \t \t \t1)-MURIPLICATION:> \n \t \t \t2)-DIVISION")
        if saisie_s1 == "1":
            Multiplication()
        elif saisie_s1=="2":
            Division()
        if saisie_s1 == "3":
            breakpoint
        if saisie_s1 =="5":
            programme_variable= False
            break
elif saisie_s =="3":
        print("\t \t Merci d'avoir utiliser ce programme*_*..........")
        programme_variable = False
