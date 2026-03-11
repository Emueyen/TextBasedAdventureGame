#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:26:25 2026

@author: Edward
"""

class CollectableItem:
    def __init__(self, Name):
        self.Name = Name

class Chest(CollectableItem):
    def __init__(self, Open, Contents):
        CollectableItem.__init__(self, "Chest")
        self.Open = Open
        self.Contents = Contents

if __name__ == "__main__":
    TestChest = Chest(False, "Spade")
    IsOpen = input("Enter Open: ")
    if IsOpen == "Open":
        TestChest.Open = True
        print("ChestOpen\n")
    OpenChest = input("Open Chest?: ")
    if OpenChest == "Y" or "Yes" and TestChest.Open == True:
        print("Chest has Been Opened")
        print("You have recieved, ", TestChest.Contents)
    