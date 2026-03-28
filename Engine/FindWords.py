#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:29:29 2026

@author: Edward
"""
def TestIn(Word, Var):
    if Word.casefold() in Var.casefold():
        return True
    else:
        return 0

def FindVerbs(var):
    Verb = ["N/A"]
    if "Hi".casefold() in var.casefold():
        print("Hi there!")
    
    #if "ABCDEFGHIJKLMOPQRSTUVWXYZ".casefold() not in var.casefold():
     #   Noun.append("N")
    
    if "show".casefold() in var.casefold():
        Verb.append("show")
    
    if TestIn("take", var) == True:
        Verb.append("take")
    
    if TestIn("Open", var) == True:
        Verb.append("open")
    
    if TestIn("attack", var) == True:
        Verb.append("attack")
    
    if TestIn("drop", var) == True:
        Verb.append("drop")
    
    if TestIn("unequip", var) == True:
        Verb.append("drop")
    
    return Verb

def FindNouns(var):
    Noun = ["N/A"]
    #North
    if TestIn("North", var) == True:
        Noun.append("N")
    
    if TestIn("Forward", var) == True:
        Noun.append("N")
    
    
    #East
    if TestIn("East", var) == True:
        Noun.append("E")
    
    if TestIn("Right", var) == True:
        Noun.append("E")
    
    
    
    #South
    if TestIn("South", var) == True:
        Noun.append("S")
    
    if TestIn("Back", var) == True:
        Noun.append("S")
    
    
    
    #West
    if TestIn("West", var) == True:
        Noun.append("W")
    
    if TestIn("Left", var) == True:
        Noun.append("W")
    
    
    
    #Equipment
    if TestIn("Items", var) == True:
        Noun.append("Equipment")

    if TestIn("Gear", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Tools", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Supplies", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Apparatus", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Kit", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Outfit", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Pack", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Loot", var) == True:
        Noun.append("Equipment")
    
    if TestIn("Bag", var) == True:
        Noun.append("Equipment")
    
    #End the Game
    if "end".casefold() in var.casefold():
        Noun.append("End")
    
    return Noun

def FindWith(var):
    IsWith = False
    if TestIn("with", var) == True:
        IsWith = True
    return IsWith