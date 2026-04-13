#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:53:57 2026

@author: Edward
"""

import pygame

pygame.init()


#Variables
WIDTH = 1000
HALFWIDTH = WIDTH/2
HEIGHT = 800
HALFHEIGHT = HEIGHT*6/10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
var = ""
Characters = pygame.image.load("Font.png")
WordsPerLine = WIDTH/32 - 1

TotalAvailableLines = HEIGHT/32

# I don't normally use AI, but I did use Gemini here to help set up this image a bit faster

# Initialize a dictionary to hold your images
LetterImages = {}

# Settings
size = 32
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def PrintLetter(char, V):
    if V[0]>WIDTH-32:
        V[0]=0
        V[1]=V[1]+32
    screen.blit(LetterImages[char], [V[0], V[1]])
    V[0] = V[0]+32
    return [V[0], V[1]]

for i, char in enumerate(alphabet):
    # Determine the row based on the character
    # A-P (0-15) are at y=128
    # Q-Z (16-25) are at y=160
    if i < 16:
        x = i * size
        y = 128
    else:
        x = (i - 16) * size  # Reset x to 0 for the second row
        y = 160
        
    rect = pygame.Rect(x, y, size, size)
    LetterImages[char] = Characters.subsurface(rect)

rect = pygame.Rect(480, 32, 32, 32)
LetterImages[" "] = Characters.subsurface(rect)

def PrintVariable(variable, x, y):
    variable = variable.upper()
    print(variable)
    for char in variable:
        try:
            if char == "\r":
                print("Enter")
                y = y+32
                x=32
                return True
            if char == "\1":
                y = y+32
                x=32
            else:
                [x, y] = PrintLetter(char, [x, y])
        except KeyError:
            print("keyerror")
            variable = variable.replace(char, "")
    return False


def FindNumber(command, x, y):
    if "\1" in command:
        print("next line")
        x = 32
        y = y-32
    if "\2" in command:
        print("next line 2")
        x = 32
        y = y-32-32-32
    return [x, y]
    

def PrintCommandLine(CL):
    x = 32
    y = 664
    print("Printing command line...")
    i=0
    for command in CL:
        i = i+1
        command = command.upper()
        try:
            [x, y] = FindNumber(command, x, y)
        except IndexError:
            print(i)
        for char in command:
            try:
                [x, y] = PrintLetter(char, [x, y])
            except KeyError:
                print("keyerror")
                command = command.replace(char, "")
        #y = y-32
        print("yay")
        


CommandLine = ["\1 Command Line again", 
               "\2 Command line test two line again", 
               "\2 Command Line test two line"]


while running == True:
    for event in pygame.event.get():
        #Type when keyup
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                var = var[:-1]
            else:
                var += event.unicode
                var = var.upper()
        
        # Check for the QUIT event, which occurs when the user clicks the close button. - Yeah right gemini
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("deepskyblue")
    
       
    
    if PrintVariable(var, 32, 664) == True:
        var = var[:-1]
        print(var)
        if len(var) > WordsPerLine:
            CommandLine.insert(0, ("\2" + var))
        else:
            CommandLine.insert(0, ("\1" + var))
        var = ""
    
    
    
    PrintCommandLine(CommandLine)
    
    print(var)
    
    pygame.display.flip()
    clock.tick(120)