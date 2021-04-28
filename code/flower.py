#!/usr/bin/python
# -*- coding:utf-8 -*-

import turtle
from polygon import arc 


def petal(t, r, angle): #t: turtle r:radius arc

    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    #t:turtle r:radius arc n:number petal, angle:radius

    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)

ecran = turtle.Screen()

anth = turtle.Turtle() 

flower(anth, 10, 120, 60)

turtle.mainloop()

