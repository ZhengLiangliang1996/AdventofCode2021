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

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day07', 'input.txt')
    l = read_txt(fn)
    lines = [int(line.rstrip()) for line in l[0].split(',')]
    print(lines)

    # brute force 
    res = 0
    f = float('inf')
    cnt = Counter(lines)
    for k in cnt.keys():
        res = 0
        for i in range(len(lines)):
            res += abs(lines[i] - k)
        f = min(f, res)
    print(f)
            
def solution2():
    fn = os.path.join(PATH, 'day07', 'input.txt')
    l = read_txt(fn)
    lines = [int(line.rstrip()) for line in l[0].split(',')]
    lines.sort()
    f = float('inf')
    for i in range(lines[0], max(lines)+1):
        res = 0
        for j in range(len(lines)):
            res += sum(list(range(1, abs(lines[j] - i)+1)))
        f = min(f, res)
    print(f)
solution2()