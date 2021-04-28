#!/usr/bin/python
# -*- coding:utf-8 -*-

"""Utilisation de l'exemple grid.py du livre pensez en python"""

# mini grille 3x3
print("+++")
print("+ +")
print("+++")

#mini grille avec des fonctions

def print_plus():
    print("+", end=' ')

def print_space():
    print(" ", end=' ')

def print_tiret():
    print("-", end=' ')

def print_bar():
    print("|", end=' ')

def print_deux(f):
    f()
    f()

def print_quatre(f):
    print_deux(f)
    print_deux(f)


