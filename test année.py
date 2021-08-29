annee = input("saisissez une année:")
try: # try me permet de gérer les exception pouvant subvenir dans la suite de mon bloc if
    annee = int (annee)
#je verifie que les restes son nuls prealablement conversion d variable et input
    assert annee > 0 #lorsque assert doit etre true sinon il renvoi une erreur cela peut me prttre de mettre par exemple une limite sur la valeur de l'année
except AssertionError :
    print("l'année saisie est inferieur ou égale à 0")
    if annee % 400 ==0 or ( annee % 4 == 0 and annee % 100 !=0):
        print("l'année que vous avez saisi est bisextile")
    else:
        print("elle n'est pas bisextile")
except ValueError :
    print("vous avez saisie une année incorrect")
except TypeError :
    print("un caratère non autorisé a été détecter dans la syntaxe de l'anné saisie")
    
