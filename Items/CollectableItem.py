#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:26:25 2026

@author: Edward
"""

from Engine.FindWords import FindNouns, FindVerbs, FindWith

class CollectableItem:
    def __init__(self, Name):
        self.Name = Name

class Chest(CollectableItem):
    def __init__(self, Open, Contents):
        CollectableItem.__init__(self, "Chest")
        self.Open = Open
        self.Contents = Contents        

class LockedChest(CollectableItem):
    def __init__(self, Open, Contents, ReqKey):
        CollectableItem.__init__(self, "Chest")
        self.Open = Open
        self.Contents = Contents
        self.ReqKey = ReqKey
    def OpenLockedChest(self, key):
        if self.ReqKey.casefold() in key.casefold():
            self.Open = True
            print("Chest Unlocked")
        else:
            print("Incorrect Key")

def OpenWith(Obj, var):
    print("you used a with!")
    Obj.OpenLockedChest(var)
    if Obj.Open == True:
        print("You have recieved, ", Obj.Contents)
        Obj.Contents = []
    

if __name__ == "__main__":
    def TestOpeningChest():
        TestChest = Chest(False, "Spade")
        IsOpen = input("Enter Open: ")
        if IsOpen == "Open":
            TestChest.Open = True
            print("ChestOpen\n")
        OpenChest = input("Open Chest?: ")
        if OpenChest == "Y" or "Yes" and TestChest.Open == True:
            print("Chest has Been Opened")
            print("You have recieved, ", TestChest.Contents)
    
    def TestOpeningLockedChest():
        TestLockedChest = LockedChest(False, "Fork", "RedKey")
        IsOpen = input("Enter Open Chest with RedKey: ")
        if "Open".casefold() in IsOpen:
            if "with".casefold() in IsOpen:
                OpenWith(TestLockedChest, IsOpen)
        else:
            print("Don't know what to open with")
        
        
        OpenChest = input("Open Chest?: ")
        if OpenChest == "Y" or "Yes" and TestLockedChest.Open == True:
            print("Chest has Been Opened")
            print("You have recieved, ", TestLockedChest.Contents)
        else:
            print("Chest is locked")
    
    TestOpeningLockedChest()
    