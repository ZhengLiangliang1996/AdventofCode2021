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
    fn = os.path.join(PATH, 'day06', 'input.txt')
    l = read_txt(fn)
    lines = [int(line.rstrip()) for line in l[0].split(',')]
    cnt = 80
    res = 0
    while cnt > 0:
        #print(lines)
            
        for i in range(len(lines)):
            lines[i] -= 1
            if lines[i] == -1:
                lines[i] = 6
                lines.append(8)

        cnt -= 1
    print(len(lines))

def solution2():
    fn = os.path.join(PATH, 'day06', 'input.txt')
    l = read_txt(fn)
    lines = [int(line.rstrip()) for line in l[0].split(',')]
    cnt = 256
    res = 0
    count = Counter(lines)
    print(count)
    while cnt > 0:
        count_1 = Counter()
        for k in count.keys():
            if k > 0:
                # dicrease only
                count_1[k-1] += count[k]
            if k == 0:
                # grow new fish
                count_1[6] += count[k]
                count_1[8] += count[k]

        count = count_1.copy()
        print(count)
        cnt -= 1

    for k in count.keys():
        res += count[k]
    print(res)
solution2()