#la ligne qui suit celle-ci est unr fonction qui demande à l'utisateur de saisir un nombre
nombre = input("saisissez un nombre:")
nombre = int (nombre)
i = 0
while i < 10:
    print(i + 1,"*",nombre,"=",( i + 1)* nombre)
    i +=1
while 1:
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break