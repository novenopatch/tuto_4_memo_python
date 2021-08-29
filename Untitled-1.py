# -*- coding: Latin-1 -*-
"""
# -*- coding: Latin-1 -*-
rien d'assez complexe le code source écrit en vue d'une relation pour une formation

#la suite directaffiche une table de mutiplication
nbr = input("\t veillez saisir un nombre")
nbr = int(nbr)
i = 0
while i <= 20:
    print("\t", nbr, "*" , i ,"=", nbr * i )
    i +=1
enter = input("Q pour quiter le programme 5 pour voir le tableau de conversion de l'euro en dollars canadien")
j = 1
 
dol = 1.65

while enter== "5" :
    while j <= 38 :
        print(j,"euro(s)","=", j * dol, "dollar(s)" )
        j +=1
    break
while enter == "Q" or "q":
    break
#la suite direct du progamme affiche une suite de nombre chaque nombre triple du précedent
w = input("Un nombre svp")
w = int(w)
g =1
while g <= 12 :
    print(w*3)
    w *= 3
    g +=1
    
"""
import os
nom  = os.getlogin()
print(nom)
print("lol")
