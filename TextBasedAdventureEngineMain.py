#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:35:30 2026

@author: Edward
"""

print("Test text based adventure game engine")

class Player:
    def __init__(self, Equipment):
        self.Equipment = Equipment
        self.Health = 10
        self.Position = [0,0]

class Tile:
    def __init__(self, Position, AvailableItems, Caption):
        self.Position = Position
        self.AvailableItems = AvailableItems
        self.CollectedItems = []
        self.Caption = Caption
    def ShowAvailableItems(self):
        print("Items in the current area: ", self.AvailableItems)
    def PrintCaption(self):
        print("    ", self.Caption)

StartTile = Tile([0, 0], ["Spoon", "Stick"], "Start Space")
Tile1 = Tile([0, 1], ["Nothing"], "1 Space North of Start")
AllTiles = [StartTile, Tile1]
StartTile.ShowAvailableItems()

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
        CompleteAction(StartTile, var)

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

def With():
    print("you used a with!")

def CheckQuickNouns(Nouns):
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
    


def CompleteAction(CurrentTile, var):
    Noun = ["N/A"]
    Verb = ["N/A"]
    IsWith = False
    
    if "Hi".casefold() in var.casefold():
        print("Hi there!")
    
    #if "ABCDEFGHIJKLMOPQRSTUVWXYZ".casefold() not in var.casefold():
     #   Noun.append("N")
    
    if "North".casefold() in var.casefold():
        Noun.append("N")
    
    if TestIn("East", var) == True:
        Noun.append("E")
    
    if TestIn("South", var) == True:
        Noun.append("S")
    
    if TestIn("West", var) == True:
        Noun.append("W")
    
    if TestIn("Equipment", var) == True:
        Noun.append("Equipment")
    
    if "end".casefold() in var.casefold():
        Noun.append("End")
    
    if "show".casefold() in var.casefold():
        Verb.append("show")
    
    if TestIn("take", var) == True:
        Verb.append("take")
    
    if TestIn("with", var) == True:
        IsWith = True
    
    
    
    AllVerbs(CurrentTile, Verb, var)
    
    if IsWith == True:
        With()
    
    if CheckQuickNouns(Noun) != 0:
        StartNewRound()
    

StartNewRound()