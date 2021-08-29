#coding:utf-8
i = False
def dire(bot ="bot", message_bot="salut !"):
    print("{} : {}".format(bot, message_bot))
dire("wiliam")
#pour eviter de répéter du code on peut simplement utilser les fontions en les créant avec (def) suivis du nom de la fonctions puis bon j'ai fais un exemple de la syntaxe en haut
def calcule_d_addition(nbr0=0,nbr1= 0,nbr2 =0,nbr3=0,nbr4=0,nbr5=0,nbr6=0,nbr7=0,nbr8=0,nbr9=0,nbr10=0):
    resultat =nbr0 + nbr1 + nbr2 + nbr3 + nbr4 + nbr5 + nbr6 + nbr7 + nbr7 + nbr8 + nbr9 + nbr10
    return resultat
#c'est ma fonction pour faire les calculs d'addition elle prend en charge 10 argument au maximum^_^,j'espère que 10 vas suffir
class fall:
    def __init__(self):
        print(" c'est ma première class")
#mon code devient un peu de désordre ^_^
print("Bienvenue dans mon programme en ligne de commande minimaliste, c'est l'un de mes premiers programme soyez donc indulgent SVP ^_^")
while i == False:
    bot = input("\t veillez saisir votre nom : ")
    print("\t Bienvenue {}".format(bot))
    #un (\t) me permet de faire une tabulation du texte(retour vers la droite
    année_actuelle = input("\t SVP, veillez enter l'année dans la quelle nous sommmes ?:")
    année_actuelle = int(année_actuelle)
    age_bot = input("\t Veillez maintenant enter votre age :")
    age_bot= int(age_bot)
    année_de_naissance_du_bot= année_actuelle - age_bot
    print("\t Votre année de naissance est alors: {}".format(année_de_naissance_du_bot))
    sortie = input("\t veillez enter 's' pour sortir de ce programme ou toutes autre lettres pour rester dans le programme:>")
    if sortie == "s" :
        print("\t Merci,,À BientÔt..........")
        i = True
    else :
        print("\t Le programme vas alors recommencer.")
        continue
#le mot break casse la boucle alors que continue la recommence, aussi les variables de type bolean sont très utile^_^
