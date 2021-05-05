#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Série infinie de pi du mathematicien :
https://en.wikipedia.org/wiki/Srinivasa_Ramanujan
"""
import math

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)

def estime_pi():
    k = 0
    total = 0
    facteur = 2 * math.sqrt(2) / 9801
    while True:
        numerateur = factoriel(4*k)*(1103 + 26390*k)
        denominateur = factoriel(k)**4 * 396**(4*k)
        term = facteur * numerateur / denominateur 
        total += term

        if abs(term) < 1e-15:
            break

        k += 1
        
    return 1 / total 
        
print(estime_pi()) 
