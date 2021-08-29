#la ligne qui suit celle-ci est unr fonction qui demande à l'utisateur de saisir un nombre
#j'ai décidé de faire de mon code de multiplication une fonction cool non*&_&*
def mutiply(*args):
    print("\t Bienvenue dans le programme affichant une table de multiplication(pouvant dépasser 10^_^) :)")
    nombre = input("\t saisissez le nombre à mutiplier>:")
    max_nbr = input("\t jusqu'a quelle nombre voulez vous que s'arrete votre table de multiplicaion????:")
    nombre = int (nombre)
    max_nbr= int(max_nbr)
    deb_multi = 0
    while deb_multi <=max_nbr:
        print(nombre,"*",deb_multi,"=",( deb_multi)* nombre)
        deb_multi +=1
    while 1:
        lettre = input("Tapez 'Q' pour quitter ou Tout autre touche pour revenir au début du programme : ")
        if lettre == "Q":
            print("Fin du programme Au revoir")
            break
