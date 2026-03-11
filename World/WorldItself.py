#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:37:07 2026

@author: Edward
"""

def CreateWorld():
    StartTile = Tile([0, 0], ["Spoon", "Stick", "Chest"], "Start Space")
    Tile1 = Tile([0, 1], ["Nothing"], "1 Space North of Start")
    AllTiles = [StartTile, Tile1]
    print("Created world successfully")
    return AllTiles

#CreateWorld()