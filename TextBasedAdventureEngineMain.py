#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:35:30 2026

@author: Edward
"""

print("Test text based adventure game engine")

from PlayerC.PC import Player
from PlayerC.QuickNouns import CheckQuickNouns
from Items.CollectableItem import CollectableItem
from World.TileClass import CreateWorld
from Engine.FindWords import FindNouns, FindVerbs, FindWith
Spoon = CollectableItem("Spoon")

AllTiles = CreateWorld()

AllTiles[0].ShowAvailableItems()

Plc = Player(["spade"])

def StartNewRound():
    print("Start New Round")
    FoundTile = 0
    for TileSpace in AllTiles:
        if TileSpace.Position == Plc.Position:
            CurrentTile = TileSpace
            CurrentTile.PrintCaption()
            FoundTile = 1
    var = input("Enter a prompt: ")
    if FoundTile == 1:
        CompleteAction(CurrentTile, var)
    else:
        CompleteAction(AllTiles[0], var)

def TestIn(Word, Var):
    if Word.casefold() in Var.casefold():
        return True
    else:
        return 0

def TakeItem(var, CurrentTile):
    for Item in CurrentTile.AvailableItems:
        if Item.casefold() in var.casefold():
            Plc.Equipment.append(Item)
            CurrentTile.AvailableItems.remove(Item)
            print("    Current Equipment: ", Plc.Equipment)
            return 0
    print("    item not found...")

def AllVerbs(CurrentTile, Verbs, var):
    for Verb in Verbs:
        if Verb == "show":
            CurrentTile.ShowAvailableItems()
        if Verb == "take":
            TakeItem(var, CurrentTile)
        if Verb == "attack":
            print("attack")
        if Verb == "drop":
            print("drop")
        if Verb == "open":
            print("open")

def With():
    print("you used a with!")
    


def CompleteAction(CurrentTile, var):
    Noun = FindNouns(var)
    Verb = FindVerbs(var)
    IsWith = FindWith(var)
    
    AllVerbs(CurrentTile, Verb, var)
    
    if CheckQuickNouns(Noun, Plc) != 0:
        StartNewRound()
        
    
    if IsWith == True:
        With()
    

StartNewRound()