# -*-coding:utf-8 -*
import os # cette ligne demande à python d'importer le module os
annee = input("saisissez une année:")
annee = int(annee)
if annee % 400 == 0 or(annee % 4==0 and annee % 100!=0):
    print("l'année que vous avez saisie est bisextile")
else:
    print("elle n'est pas bisextile")
os.system("pause")
