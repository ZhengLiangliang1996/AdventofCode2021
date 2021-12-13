#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import collections
import os
from collections import Counter
import re
import matplotlib.pyplot as plt
import numpy as np
PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

# fold 7 

# 8 -> 6 (8-2) 8 - (8 - (7))*2
# 9 -> 5 (9-4) 
# 10 -> 4 (10-6)
# 11 -> 3 (11-8)
# 14 -> 0 (14-14) 14 - (14-7)*2

def fold_help(brd, c, f_num):
    brd_new = set()
    for brd_sub in brd:
        a,b = brd_sub[0], brd_sub[1]
        if c == 'x' and a == f_num: continue
        if c == 'y' and b == f_num: continue 
        if c == 'x' and a > f_num:
            a = a - ((a - f_num) * 2)
        if c == 'y' and b > f_num:
            b = b - ((b - f_num) * 2)
        # discard the one with the same with 
        brd_new.add((a, b))
    return brd_new 

def solution1():
    fn = os.path.join(PATH, 'day13', 'input.txt')
    l = read_txt(fn)
    lines = ''.join(l)
    points, fold = lines.split('\n\n')
    points = [x for x in points.split('\n')]
    num_reg = re.compile(r'fold along ([x|y])=(\d{1,10})')
    # draw brd 
    brd = set()
    for p in points:
        p1, p2 = p.split(',')
        brd.add((int(p1), int(p2)))
    
    print(brd)
    res = 0
    for f in fold.split('\n'):
        if f:
            coor = num_reg.findall(f)[0]
            c, f_num= coor[0], int(coor[1])

            brd = fold_help(brd, c, f_num)
            break
    
    print(brd)

def solution2():
    fn = os.path.join(PATH, 'day13', 'input.txt')
    l = read_txt(fn)
    lines = ''.join(l)
    points, fold = lines.split('\n\n')
    points = [x for x in points.split('\n')]
    num_reg = re.compile(r'fold along ([x|y])=(\d{1,10})')
    # draw brd 
    brd = set()
    for p in points:
        p1, p2 = p.split(',')
        brd.add((int(p1), int(p2)))
    
    res = 0
    for f in fold.split('\n'):
        if f:
            coor = num_reg.findall(f)[0]
            c, f_num= coor[0], int(coor[1])

            brd = fold_help(brd, c, f_num)

    max_x, max_y = -1, -1
    for b in brd:
        max_x = max(max_x, b[0])
        max_y = max(max_y, b[1])

    brd = list(brd)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in brd:
                print('*', end='*')
            else:
                print(' ', end='_')
        print(' ')
    #print()
    # brd = list(brd)
    # data_in_array = np.array(brd)
    # transposed = data_in_array.T
    # x, y = data_in_array 
    # fig, ax = plt.subplots(1,1) 
    # ax.plot(x, y, 'ro')
    # fn_image = os.path.join(PATH, 'day13', 'a.png')
    # fig.savefig(fn_image)

solution2()