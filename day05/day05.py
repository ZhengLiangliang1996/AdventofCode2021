#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os
from collections import Counter

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day05', 'input.txt')
    l = read_txt(fn)
    lines = [line.rstrip() for line in l]
    coordidates = []
    for l in lines:
        c1, c2 = l.split(' -> ')

        x1, y1 = [int(x) for x in c1.split(',')]
        x2, y2 = [int(x) for x in c2.split(',')]
        # lines where either x1 = x2 or y1 = y2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                coordidates.append((x1, y))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                coordidates.append((x, y1))
    res = 0 
    # count 
    cnt = Counter(coordidates)
    print(cnt)
    for c in cnt:
        if cnt[c] >= 2:
            print(cnt[c])
            res += 1
    
    print(res)
def solution2():
    fn = os.path.join(PATH, 'day05', 'input.txt')
    l = read_txt(fn)
    lines = [line.rstrip() for line in l]
    coordidates = []
    for l in lines:
        c1, c2 = l.split(' -> ')

        x1, y1 = [int(x) for x in c1.split(',')]
        x2, y2 = [int(x) for x in c2.split(',')]
        # lines where either x1 = x2 or y1 = y2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                coordidates.append((x1, y))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                coordidates.append((x, y1))

        # diaganal 
        if (x1 > x2 and y1 > y2):
            while x1+1 != x2:
                coordidates.append((x2, y2))
                x2 += 1
                y2 += 1
                

        elif x1 < x2 and y1 < y2:
            while x1-1 != x2:
                coordidates.append((x2, y2))
                x2 -= 1
                y2 -= 1
                
        elif x1 > x2 and y1 < y2:
            while x1+1 != x2:
                coordidates.append((x2, y2))
                x2 += 1
                y2 -= 1
                
        elif x1 < x2 and y1 > y2:
            while x1-1 != x2:
                coordidates.append((x2, y2))
                x2 -= 1
                y2 += 1

    res = 0 
    # count 
    cnt = Counter(coordidates)

    for c in cnt:
        if cnt[c] >= 2:
            print(cnt[c])
            res += 1
    print(res)
    

solution2()