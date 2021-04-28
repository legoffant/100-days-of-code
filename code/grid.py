#!/usr/bin/python
# -*- coding:utf-8 -*-

"""Utilisation de l'exemple grid.py du livre pensez en python"""

# mini grille 3x3
print("+++")
print("+ +")
print("+++")

#mini grille avec des fonctions

def print_beam():
    print("+----", end=' ')

def print_post():
    print("|    ", end=' ')

def print_deux(f):
    f()
    f()

def print_quatre(f):
    print_deux(f)
    print_deux(f)

def print_beams():
    print_deux(print_beam)
    print("+")

def print_posts():
    print_deux(print_post)
    print("|")

def print_row():
    print_beams()
    print_quatre(print_posts)

def print_grid():
    print_deux(print_row)
    print_beams()

print_grid()
