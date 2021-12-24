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

def solution1():
    fn = os.path.join(PATH, 'day24', 'input.txt')
    l = read_txt(fn)
    
    FOUND = True 


# here I take it down what I wrote in paper : )         
# can see from the pattern when parsing the instructions one by one 
# x will be cancel out back to 0 if add x ## > 10

# z = d0+6
# z = (d0+6) * 26 + d1 + 14
# z = ((d0+6) * 26 + d1+14) * 26 + d2 + 13
# in the fourth part we have our first subjection 
# d3 == d2 + 13 -14 => d3 == d2 - 1

# So if we found that z keeps doing *26 and mod 26 operations 
# when we see add x is negative, we choose from the last term 
# in z (which could be think of as stack, now interpreted as x) - a number #
# and it should be equal to the w. 
# So we have 

# w == (last term of z) - number 

# so for y term, we only keep track of what is the last term for it
# it is involve with w and only change with 'add' if we found add x 
# is positive

# we have 
# FIRST PART 
# w = d0, x= 0, y = 0, z = 0
# inp w
# mul x 0 w = d0, x= 0, y = 0, z = 0
# add x z w = d0, x= 0, y = 0, z = 0
# mod x 26 w = d0, x= 0, y = 0, z = 0
# div z 1 w = d0, x= 0, y = 0, z = 0
# add x 11 w = d0, x= 0, y = 11, z = 0
# eql x w w = d0, x= 0, y = 0, z = 0
# eql x 0 w = d0, x= 1, y = 0, z = 0
# mul y 0 w = d0, x= 1, y = 0, z = 0
# add y 25 w = d0, x= 1, y = 25, z = 0
# mul y x w = d0, x= 1, y = 25, z = 0
# add y 1 w = d0, x= 1, y = 26, z = 0
# mul z y w = d0, x= 1, y = 26, z = 0
# mul y 0 w = d0, x= 1, y = 0, z = 0
# add y w w = d0, x= 1, y = d0, z = 0
# add y 6 w = d0, x= 1, y = d0+6, z = 0
# mul y x w = d0, x= 1, y = d0+6, z = 0
# add z y w = d0, x= 1, y = d0+6, z = d0+6

# Second  PART   
# w = d1, w = d1, x= 1, y = d0+6, z = d0+6
# inp w  w = d1, x= 1, y = d0+6, z = d0+6
# mul x 0 w = d1, x= 0, y = d0+6, z = d0+6
# add x z w = d1, x= d0+6, y = d0+6, z = d0+6
# mod x 26 w = d1, x= (d0+6)%26, y = d0+6, z = d0+6
# div z 1 w = d1, x= (d0+6)%26, y = d0+6, z = d0+6
# add x 11 w = d1, x= (d0+6)%26 + 11, y = d0+6, z = d0+6
# eql x w w = d1, x= 0, y = d0+6, z = d0+6
# eql x 0 w = d1, x= 1, y = d0+6, z = d0+6
# mul y 0 w = d1, x= 1, y = 0, z = d0+6
# add y 25 w = d1, x= 1, y = 25, z = d0+6
# mul y x w = d1, x= 1, y = 25, z = d0+6
# add y 1 w = d1, x= 1, y = 26, z = d0+6
# mul z y w = d1, x= 1, y = 26, z = (d0+6) * 26
# mul y 0 w = d1, x= 1, y = 0, z = (d0+6) * 26
# add y w  w = d1, x= 1, y = d1, z = (d0+6) * 26
# add y 14 w = d1, x= 1, y = d1+14, z = (d0+6) * 26
# mul y x w = d1, x= d1+14, y = d1+14, z = (d0+6) * 26
# add z y x= d1+14, y = d1+14, z = (d0+6) * 26 + d1+14

# THIRD PART 
# w = d2, x= d1+14, y = d1+14, z = (d0+6) * 26 + d1+14
# mul x 0 x= 0, y = d1+14, z = (d0+6) * 26 + d1+14
# add x z x= (d0+6) * 26 + d1+14, y = d1+14, z = (d0+6) * 26 + d1+14
# mod x 26 x= d1+14, y = d1+14, z = (d0+6) * 26 + d1+14
# div z 1 x= d1+14, y = d1+14, z = (d0+6) * 26 + d1+14
# add x 15 x= (d1+14) + 15, y = d1+14, z = (d0+6) * 26 + d1+14
# eql x w x= 0, y = d1+14, z = (d0+6) * 26 + d1+14
# eql x 0 x= 0, y = d1+14, z = (d0+6) * 26 + d1+14
# mul y 0 x= 0, y = 0, z = (d0+6) * 26 + d1+14
# add y 25 x= 0, y = 25, z = (d0+6) * 26 + d1+14
# mul y x x= 0, y = 25, z = (d0+6) * 26 + d1+14
# add y 1 x= 0, y = 26, z = (d0+6) * 26 + d1+14
# mul z y x= 0, y = 26, z = ((d0+6) * 26 + d1+14) * 26
# #...
# add z y  z = ((d0+6) * 26 + d1+14) * 26 + d2 + 13


# FOURTH PART 
# w = d3, x= d1+14, y = d1+14, z = (((d0+6) * 26 + d1+14) * 26 + 13) * 26

# mul x 0 x= 0, y = d2+13, z = (((d0+6) * 26 + d1+14) * 26 +d2 + 13) * 26
# add x z  x= 0, y = d2+13, z = (((d0+6) * 26 + d1+14) * 26 +d2 + 13) * 26
# mod x 26 x= d2+13, y = d2+13, z = (((d0+6) * 26 + d1+14) * 26 +d2 + 13)
# div z 26 x= d2+13, y = d2+13, z = d0 + 6 + d1 + 14
# add x -14 x= d2+13 -14, y = d2+13, z = d0 + 6 + d1 + 14
# eql x w x= d2+13 -14, y = d2+13, z = d0 + 6 + d1 + 14
# eql x 0 
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 1
# mul y x
# add z y



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


    # variables = {'w':0, 'x':0, 'y':0, 'z':0}
    # NOT ABLE TO SOLVE IT 
    # s = Optimize()
    ## 
    # def chk_var(b):
    #     if b.isdigit():
    #         return int(b)
    #     else:
    #         return variables[b]

    # res = [] 
    # for line in l:
    #     ins = line.rstrip().split(' ') 
    #     if ins[0] == 'inp':
    #         w = Int('w')
    #         res.append(w)
    #         variables[ins[1]] = w
    #         s.add(w >= 0, w <= 9)
    #     elif ins[0] == 'add':
    #         variables[ins[1]] = variables[ins[1]] + chk_var(ins[2])
    #     elif ins[0] == 'mul':
    #         variables[ins[1]] = variables[ins[1]] * chk_var(ins[2])
    #     elif ins[0] == 'div':
    #         variables[ins[1]] = math.floor(variables[1] / chk_var(ins[2]))
    #     elif ins[0] == 'mod':
    #         variables[ins[1]] = variables[ins[1]] % chk_var(ins[2])
    #     elif ins[0] == 'eql':
    #         variables[ins[1]] = 1 if variables[ins[1]] == chk_var(ins[2]) else 0
    #     else:
    #         pass 

solution1()