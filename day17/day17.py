#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import collections
import os
import re
import numpy as np

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

# target area: x=257..286, y=-101..-57
def solution1():
    
    # brute fore 
    res = 0 
    cnt = 0
    # search space: starting pos: 0, left bound > 0, x_v start from positive
    # same for x_y:  -101  <-0-> 101
    # velocity
    # for i in range(1, 287+1):
    for i in range(1,287+1):
        # symmetric 
        
        for j in range(-101, 101):
        #for j in range(-101-1, 101+1+1000):
            x, y, x_v, y_v = 0, 0, i, j  
            y_max = 0
            FOUND = False  
            for _ in range(500):
                x += x_v 
                y += y_v 
                
                # decrease 
                x_v -= 1
                y_v -= 1 
                # can not be less than 0
                x_v = max(0, x_v)
                y_max = max(y_max, y)
                # x=20..30, y=-10..-5
                #target area: x=257..286, y=-101..-57
                if 257<= x <= 286 and -101 <= y <= -57:
                    FOUND = True 
                    cnt += 1
                    break

            if FOUND:
                res = max(res, y_max)
                print(x_v, y_v, res, cnt) 

solution1()