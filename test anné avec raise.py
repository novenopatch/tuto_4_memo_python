annee = input("saisissez une année:")
try: # try me permet de gérer les exception pouvant subvenir dans la suite de mon bloc if
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
