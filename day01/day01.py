#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    return lines 

def solution1():
    fn = os.path.join(PATH, 'day01', 'input.txt')
    l = read_txt(fn)
    
    print(l)
    res = 0
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            res += 1
    
    print(res)

def solution2():
    fn = os.path.join(PATH, 'day01', 'input.txt')
    l = read_txt(fn)
    print(l)
    res = 0
    for i in range(1, len(l)-2):
        a = l[i+2]
        b = l[i-1]
        if a > b:
            res += 1

    print(res)
solution2()
