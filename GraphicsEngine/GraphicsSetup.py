#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:53:57 2026

@author: Edward
"""

import pygame

pygame.init()


#Variables
WIDTH = 800
HALFWIDTH = WIDTH/2
HEIGHT = 800
HALFHEIGHT = HEIGHT*6/10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
var = ""
Characters = pygame.image.load("Font.png")

# I don't normally use AI, but I did use Gemini here to help set up this image a bit faster

# Initialize a dictionary to hold your images
LetterImages = {}

# Settings
size = 32
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

while running == True:
    for event in pygame.event.get():
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
    
    x = 0
    for char in var:
        try:
            screen.blit(LetterImages[char], [x, 0])
            x = x+32
        except KeyError:
            print("keyerror")
            var = var.replace(char, "")
            
    
    print(var)
    
    pygame.display.flip()
    clock.tick(120)
