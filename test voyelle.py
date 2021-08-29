chaine = input("saisissez une chaine de caratère:")
for lettre in chaine:
    if lettre in "AEIOUYaeiouy":
        print(lettre)
    else :
         print("*")
