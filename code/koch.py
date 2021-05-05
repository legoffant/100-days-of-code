#!/usr/bin/python
# -*- coding:utf-8 -*-

from turtle import *
"""
def decale_vers_la_gauche(largeur):
    left(180)
    penup()
    forward(largeur)
    pendown()
    left(180)

def decale_vers_le_haut(hauteur):
    left(90)
    penup()
    forward(hauteur)
    pendown()
    right(90)
"""
def koch(n, longueur):
    speed(0)
    pencolor("blue")

    if n == 0:
        forward(longueur)
    else:
        koch(n - 1, longueur /3)
        left(60)
        koch(n - 1, longueur /3)
        right(120)
        koch(n - 1, longueur /3)
        left(60)
        koch(n - 1, longueur /3)

def flocon(n,longueur):
    for i in range(3):
        koch(n, longueur)
        right(120)

#ecran = turtle.Screen()
#anth = turtle.Turtle()

#decale_vers_la_gauche(300)
#decale_vers_le_haut(-200)

penup()
goto(-200, -200)
pendown()
flocon(4, 300) 

#turtle.mainloop()

