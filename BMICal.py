# -*- coding: utf-8 -*-
'''
version:python 2.7
author:Deadmorning
system:win64
'''
weight=raw_input('体重(公斤)：')
height=raw_input('身高（米）：')
a = float(weight)/(float(height)*float(height))
if a < 18.5:
    print "体重偏轻"
if a >= 18.5 and a < 24 :
    print "体重正常"
if a >= 24 :
    print '体重偏重'