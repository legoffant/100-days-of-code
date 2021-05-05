#!/usr/bin/python
#-*- coding:utf-8 -*-

def compteur(mot, a):
    compteur = 0
    for lettre in mot:
        if lettre == a:
            compteur = compteur + 1
    print(compteur)

compteur("test", 't')


