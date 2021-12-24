#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 
import copy 
import math 
import re
import itertools
import collections
import functools
import sys
from z3 import *
sys.setrecursionlimit(1500)

PATH = '/Users/liangliang/Desktop/AdventOfCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines 



# inp a - Read an input value and write it to variable a.
# add a b - Add the value of a to the value of b, then store the result in variable a.
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

# (Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute
#  mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

'''
inp0 += 6
inp1 += 14
inp2 += 13
inp3 == inp2 - 14 
inp4 += 6
inp5 == inp4 - 0
inp6 == inp1 - 6 
inp7 += 3
inp8 == inp7  - 3
inp9 += 14 
inp10 += 4 
inp11 == inp10 - 2
inp12 == inp9 - 9 
inp13 == inp0 - 2 
'''


'''
inp3 == inp2 - 1 
inp5 == inp4 + 6
inp6 == inp1 + 8 
inp8 == inp7
inp11 == inp10 + 2
inp12 == inp9 + 5 
inp13 == inp0 + 4 
'''

'''
inp3 == inp2 - 1   
  8      9 
inp5 == inp4 + 6
  9      3
inp6 == inp1 + 8 
  9      1
inp8 == inp7       
  9      9
inp11 == inp10 + 2 
  9          7
inp12 == inp9 + 5  
  9         4
inp13 == inp0 + 4  
  9        5
'''
# 51983999947999


'''
inp3 == inp2 - 1   
  1      2 
inp5 == inp4 + 6
  7      1
inp6 == inp1 + 8 
  9      1
inp8 == inp7       
  1      1
inp11 == inp10 + 2 
  3        1
inp12 == inp9 + 5  
  6        1 
inp13 == inp0 + 4  
  5        1
'''
# 11211791111365

