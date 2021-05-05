#!/usr/bin/python


def compter_mot(nombre):
    compteur = 0
    while (compteur <= nombre):
        compteur += compteur

def afficher_mot(mot):
    if len(mot) >= 14:
        print(mot)


fichier = open("scrabble.txt", "r", encoding="utf-8") 
compteur = 0
for ligne in fichier:
    mot = ligne.strip()
    compteur += 1 + mot 
    print("ici!")
    print(compteur)
    if compteur <= 20 and len(mot) >= 14:
        print(mot)
    print("ici2")





    
