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
        lines = [line.rstrip() for line in lines]

    return lines 

def solution1():
    fn = os.path.join(PATH, 'day02', 'input.txt')
    l = read_txt(fn)
    h, d = 0, 0
    for i in l:
        print(i)
        dir, num = i.split(" ")
        if dir == 'forward':
            h += int(num)
        if dir == 'down':
            d += int(num)
        if dir == 'up':
            d -= int(num)
    print(h, d)
    print(max(h*d, 0))


def solution2():
    fn = os.path.join(PATH, 'day02', 'input.txt')
    l = read_txt(fn)
    h, d, aim = 0, 0, 0
    for i in l:
        print(i)
        dir, num = i.split(" ")
        if dir == 'forward':
            h += int(num)
            if aim != 0:
                d += int(num) * aim
        if dir == 'down':
            aim += int(num)
        if dir == 'up':
            aim -= int(num)
    print(h, d)
    print(max(h*d, 0))

    
solution2()