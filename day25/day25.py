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
sys.setrecursionlimit(1500)

PATH = '/Users/liangliang/Desktop/AdventOfCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day25', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    brd = []
    i, j = -1, -1
    for line in l.split('\n'):
        b = []
        if line:
            for sub_line in line:
                b.append(sub_line)
        brd.append(b)
    brd.pop()
    print(brd)
    step = 0
    freeze = False
    m, n = len(brd), len(brd[0])
    
    while not freeze:
        step += 1
        new_brd = copy.deepcopy(brd)
        cnt = 0
        print(step)
        # move east 
        for i in range(m):
            for j in range(n):
                # could move right 
                # print(m, n, (j+1)%n)
                if brd[i][j%n] == '>' and brd[i][(j+1)%n] == '.': 
                    new_brd[i][(j+1)%n] = '>'
                    new_brd[i][j%n] = '.'
                    cnt += 1
                    
        # then move south 
        new_new_brd = copy.deepcopy(new_brd)
        for i in range(m):
            for j in range(n):
                if new_brd[i%m][j] == 'v' and new_brd[(i+1)%m][j] == '.':
                    new_new_brd[(i+1)%m][j] = 'v'
                    new_new_brd[(i)%m][j] = '.'
                    cnt += 1
        brd = copy.deepcopy(new_new_brd)
        if cnt == 0:
            freeze = True 
    print(step)

def solution2():
    fn = os.path.join(PATH, 'day25', 'input.txt')
    # l = read_txt(fn)
    # l = ''.join(l)
    # a = l.split('\n\n')
    p1_pos, p1_s = 7, 0
    p2_pos, p2_s = 6, 0
    # roll = 1



 
solution1()