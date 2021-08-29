import os
#la ligne qui suit celle-ci est unr fonction qui demande à l'utisateur de saisir un nombre
#j'ai décidé de faire de mon code de multiplication une fonction cool non*&_&*
def mutiply(*args):
    print("\t Bienvenue dans le programme affichant une table de multiplication(pouvant dépasser 10^_^)  :)")
    nombre = input("\t saisissez le nombre>:")
    nombre = int (nombre)
    i = input("\t jusqu'a quelle nombre voulez vous que s'arrete votre table de multiplicaion????:")
    i= int(i)
    deb_multi = 0
    while deb_multi <=i:
        print(nombre +1,"*",deb_multi,"=",( deb_multi + 1)* nombre)
        deb_multi +=1
    while 1:
        lettre = input("Tapez 'Q' pour quitter ou Tout autre touche pour revenir au début du programme : ")
        if lettre == "Q":
            print("Fin du programme Au revoir")
            break
mutiply()
os.system("pause")