
"""ceci est mon programme en ligne de commande de calcul de base"""
#fonction de calcul
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
    print("\t {}/{} = {} avec {} comme reste.......".format(nbr0, nbr1, resultat, reste)