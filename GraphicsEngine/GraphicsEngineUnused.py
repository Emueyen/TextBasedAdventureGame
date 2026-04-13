#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:44:05 2026

@author: edward
"""

def PrintVariableBottomUp(variable, x, y):
    variable = variable.upper()
    print("printing ", variable, "from the bottom up")
    for char in variable:
        try:
            if char == "\1":
                print("next line")
                x=32
                y = y-32
            if char == "\2":
                print("next line 2")
                x=32
                y = y-64
            if y>HEIGHT:
                print("went off screen")
                return 0
            else:
                [x, y] = PrintLetter(char, [x, y])
        except KeyError:
            print("keyerror")
            variable = variable.replace(char, "")
            
StartingText = "Welcome to a test for \1 the graphics engine"
PrintVariable(StartingText, 0, 0)