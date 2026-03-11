#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:21:28 2026

@author: Edward
"""

def CheckQuickNouns(Nouns, Plc):
    Found = 0
    for Noun in Nouns:
        #Movement
        if Noun == "N":
            Plc.Position[1] = Plc.Position[1] + 1
            print("    Moved North, current position: ", Plc.Position)
            Found = 1
        if Noun == "S":
            Plc.Position[1] = Plc.Position[1] - 1
            print("    Moved South, current position: ", Plc.Position)
            Found = 1
        if Noun == "E":
            Plc.Position[0] = Plc.Position[0] + 1
            print("    Moved East, current position: ", Plc.Position)
            Found = 1
        if Noun == "W":
            Plc.Position[0] = Plc.Position[0] - 1
            print("    Moved West, current position: ", Plc.Position)
            Found = 1
        if Noun == "Equipment":
            print("    Current Equipment: ", Plc.Equipment)
            Found = 1
        
        if Noun == "End":
            print ("Game end")
            Found = 1
            return 0
    if Found == 0:
        return 1
        #print("No relevant Quick Noun was found")