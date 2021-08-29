import os
from random import randrange
from math import ceil
argent = 200
continuer_partie = True
nb = input("                 saisissez svp un numéro compris entre 0 et 49:")
mise = input("               saisissez votre mise inférieur ou égal à 200'$':")
mise = int(mise)
nb = int(nb)
mise = int(mise)
while continuer_partie == True :
    if mise <= 200:
        while nb > 0 and nb >= 49:
            numero_g =randrange(50)
            print("ça tourne ça tourne....................")
            if numero_g == nb:
                                print("gagnez,. vous obtez", mise * 3,"$")
                                argent = mise * 3 +argent
                                print("maintenant vous avez",argent)
            elif numero_g % 2 == nb % 2:# le nbr gagnant est de meme couleur que nb
                                mise = mise/2
                                argent = mise + argent
                                print("vous aves misé sur la bonne couleur")
                                print("vous avez maintenant",argent)
            else:
                                print("vous avez perdu, votre mise est alors nul")
                                argent = argent - mise
                                print("maintenant vous avez",argent)
            if argent <= 0:
                                print("vous avez perdu tout votre argent")
                                quiter = input("souhaitez-vous quiter le casino (o/n) ? :")
                                if quiter == "o" or quiter == "O":
                                    print("vous quitez le casino avec vos gains.................................")
                                    continuer_partie = False
                                    break
            print("vous avez à présent",argent,"$")
            quiter = input("souhaitez-vous quiter le casino (o/n) ? :")
            if quiter == "o" or quiter == "O":
                                print("vous quitez le casino avec vos gains.")
                                continuer_partie = False
                                break
            else :
                                nb = input("saisissez à nouveau svp un numéro compris entre 0 et 49")
                                mise = input("saisissez votre mise inférieur ou égal à votre argent:")
                                mise = int(mise)
                                nb = int(nb)
                                continue
os.sytem("pause")
                
                
