#!/usr/bin/python
# -*- coding:utf-8 -*-

"""effectuer une recherche"""

def trouver(mot, lettre):
    index = 0
    while index < len(mot):
        if mot[index] == lettre:
            return index
        index = index + 1
    return - 1

trouver("test",'e')
