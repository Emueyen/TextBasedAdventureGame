#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:30:03 2026

@author: Edward
"""

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

def CreateWorld():
    StartTile = Tile([0, 0], ["Spoon", "Stick", "Chest"], "Start Space")
    Tile1 = Tile([0, 1], ["Nothing"], "1 Space North of Start")
    AllTiles = [StartTile, Tile1]
    print("Created world successfully")
    return AllTiles