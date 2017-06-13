# -*- coding: utf-8 -*-
'''
version:python 2.7
author:Deadmorning
system:win64
'''
import random
CardNum =['1','2','3','4','5','6','7','8','9','10','J','Q','K']
King =['King','Queen']
Colour =['spades','clubs','diamonds','hearts']
for x in CardNum:
    for y in Colour:
        poker = y + x
        King.append(poker)
random.shuffle(King)

'''Back To Childhood'''
Player1 = King[0:16]
Player2 = King[17:33]
Player3 = King[34:50]
BottomCard = King[51:54] 
print Player1
print Player2
print Player3
print BottomCard

'''Checking cheat'''
set1 = set(Player1)
set2 = set(Player2)
set3 = set(Player3)
set4 = set(BottomCard)
print set1 & set2 & set3 & set4