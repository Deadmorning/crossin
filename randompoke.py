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
print len(King)
Player1= []
Player2= []
Player3= []
i = 0
while i < 17:
    a = random.choice(King)
    Player1.append(a)
    King.remove(a)
    b = random.choice(King)
    Player2.append(b)
    King.remove(b)
    c = random.choice(King)
    Player3.append(c)
    King.remove(c)
    i = i + 1
print Player1 
print Player2 
print Player3
print King
set1 = set(Player1)
set2 = set(Player2)
set3 = set(Player3)
set4 = set(King)
print set1 & set2 & set3 & set4