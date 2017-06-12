# -*- coding: utf-8 -*-
'''
version:python 2.7
author:Deadmorning
system:win64
'''

people = int(input('红包个数:\n'))
money = int(input('红包金额:\n')*100)
import random
def redpacket(people,money):
    result = []
    remain = people
    max_money = money/people*2
    for i in range(people):
        remian = remain - 1
        if remain > 0:
            m = random.randint(1,min(money - remain,max_money))
        else:
            m = money
        money = money - m
        result.append(m / 100.0)
    return result
print redpacket(people,money)