#!/usr/bin/python
#-*- coding:utf-8 -*-

fichier = open("scrabble.txt", "r", encoding="utf-8") 
compteur = 0
for ligne in fichier:
    mot = ligne.strip()
    if  len(mot) >= 14:
        print(mot)
        compteur += 1
        if compteur == 21:
            break






    
