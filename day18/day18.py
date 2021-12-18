#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os

import numpy as np
import ast
import math
PATH = '/Users/liangliang/Desktop/AdventofCode2021'

# class Tree:
#     def __init__(self):
#         self.root = None 
#         self.left = None 
#         self.right = None 
#         self.parent = None 
#         self.val = None

# TODO: Binary tree to implement explode 

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

def addition(s1, s2):
    # [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].
    return chk([s1, s2])

def split(s):
    # >= 10
    # To split a regular number, replace it with a pair; the left element of the pair 
    # should be the regular number divided by two and rounded down, while the right element of 
    # the pair should be the regular number divided by two and rounded up.
    # base case 
    # [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    if isinstance(s, int):
        if s >= 10:
            return True, [s//2, math.ceil(s/2)]
        else:
            return False, s
    elif isinstance(s, list): #list 
        #  F      [0,7]           [0,7]
        splitable, s1 = split(s[0])
        if splitable:          
            return splitable, [s1, s[1]]
        else:
            #     F     4              4
            splitable2, s2 = split(s[1])
            return splitable2, [s1, s2]
                              # [[0,7], 4]
def chk(s):
    # chk explode or split is possible 
    #     If any pair is nested inside four pairs, the leftmost such pair explodes.
    # If any regular number is 10 or greater, the leftmost such regular number splits.
        # explode -> explode -> split -> explode 
    ITER = True 
    while ITER: 
        iterable, s = explode(s)    
        if iterable:
            continue 
        
        iterable, s = split(s)
        print(s)
        if not iterable:
            ITER = False
    return s 

def explode(s):
    s = str(s)
    global_string = []
    i = 0
    while i < len(s):
        #print(i)
        if s[i].isdigit():
            num = int(s[i])
            while i+1 < len(s) and s[i+1].isdigit():
                num = num * 10 + int(s[i+1])
                i += 1    
            global_string.append(num)
            i += 1
        elif s[i] == ' ' or s[i] == "'":
            i += 1
        else: 
            global_string.append(s[i])
            i += 1
    print(global_string)
    l_b_num = 0
    for i in range(len(global_string)): 
        if global_string[i] == '[':
            l_b_num += 1
        elif global_string[i] == ']':
            l_b_num -= 1
        if l_b_num == 5:
            old_s = global_string.copy()
            l = global_string[i+1]
            r = global_string[i+3]
            left_first, right_first = -1, -1

            for j in range(i+4, len(old_s)):
                if isinstance(global_string[j], int): 
                    right_first = j
                    break 
            if j == len(old_s) - 1: right_first = -1
            
            for j in range(i-1, -1, -1):
                if isinstance(global_string[j], int): 
                    left_first = j 
                    break
            if j == 0: left_first = -1
            
            if right_first != -1:
                global_string[right_first] += r
                
            global_string = global_string[:i] + ['0'] + global_string[i+5:]

            if left_first != -1:
                global_string[left_first] += l
            print(global_string)
            a = [str(x) for x in global_string]
            a = ''.join(a)
            return True, ast.literal_eval(a)

    a = [str(x) for x in global_string]
    a = ''.join(a)
    return False, ast.literal_eval(a)


def magnitude(s):
    # base case int 
    if isinstance(s, int):
        return s
    else:
        s1 = 3 * magnitude(s[0]) + 2 * magnitude(s[1])
        return s1
        
def solution1():
    fn = os.path.join(PATH, 'day18', 'input.txt')
    l = read_txt(fn)
    a = [ast.literal_eval(x) for x in l if x != '\n' or x != ' ']
    
    # print(explode('[[[[[9,8],1],2],3],4]'))
    # temp = ast.literal_eval('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    # explode(temp)
    #split(temp)
    #print(temp)
    temp = a[0]
    for i in range(1, len(a)):
        temp = addition(temp, a[i])
        temp = chk(temp)
    print(temp)
    
    print(magnitude(temp))

def solution2():
    fn = os.path.join(PATH, 'day18', 'input.txt')
    l = read_txt(fn)
    a = [ast.literal_eval(x) for x in l if x != '\n' or x != ' ']
    max_num = float('-inf')
    for i in range(len(a)):
        for j in range(i,len(a)):
            if i != j:
                temp = addition(a[i], a[j])
                temp = chk(temp)
                max_num = max(max_num, magnitude(temp))
    print(max_num)


solution2()     
