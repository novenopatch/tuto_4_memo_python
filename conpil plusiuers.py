santa= 8
print(santa)
nouritures = ['pomme de terre','riz au gras','ayimolou']
loisires = ['dormir','gaming sur android','la programation web en html']
favoris = loisires + nouritures
print(favoris)
n1 = "Kokou Amétépé joseph"
n2 ="HOMAWOO"
texte_blague = '''bonjour %s %s.
bonjour comment vas tu Mr luck'''
print(texte_blague %(n2,n1))
age = input('tapez svp votre age:')
age = int(age)
if age >18:
    print("majeur")
else :
    print("jeune")
annee = input("saisissez une année:")
annee = int (annee)
#je verifie que les restes son nuls prealablement conversion d variable et input
if annee % 400 ==0 or ( annee % 4 == 0 and annee % 100 !=0):
    print("l'année que vous avez saisi est bisextile")
else:
   print("elle n'est pas bisextile")
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
