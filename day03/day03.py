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
        lines = [line.rstrip() for line in lines]

    return lines 

def solution1():
    fn = os.path.join(PATH, 'day03', 'input.txt')
    l = read_txt(fn)
    res = ''
    for i in range(len(l[0])):
        a = ''
        cnt = None
        for j in l:
            a += str(j[i])

        cnt = Counter(str(a))
        res += cnt.most_common(1)[0][0]

    res1 = ''.join('1' if x == '0' else '0' for x in res)

    print(int(res, base=2)*int(res1, base=2))


def solution2():
    fn = os.path.join(PATH, 'day03', 'input.txt')
    l = read_txt(fn)
    ogr = l.copy()
    co2 = l.copy()
    for i in range(len(l[0])):
        a = ''
        cnt = None
        if len(ogr) == 1:
                break
        for j in ogr:
            a += str(j[i])

        cnt = Counter(str(a))
        # If 0 and 1 are equally common, keep values with a 1 in the position being considered.
        a = cnt.most_common(1)[0][0]
        b = cnt.most_common(2)[1][0]
        print(ogr)
        if a == b:
            a = '1'
        if len(ogr) > 1:
            ogr = [x for x in ogr if x[i] == a]

    print(ogr)
    for i in range(len(l[0])):
        a = ''
        cnt = None
        if len(co2) == 1:
                break
        for j in co2:
            
            a += str(j[i])

        cnt = Counter(str(a))
        # If 0 and 1 are equally common, keep values with a 0 in the position being considered.
        a = cnt.most_common(1)[0][0]
        b = cnt.most_common(2)[1][0]

        if a == b:
            b = '0'
        
        if len(co2) > 1:
            co2 = [x for x in co2 if x[i] == b]

    print(int(ogr[0], base=2)*int(co2[0], base=2))

solution2()
