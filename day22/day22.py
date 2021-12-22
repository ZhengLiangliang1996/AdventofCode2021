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


def chk_overlap(x1, x2, x_new1, x_new2):
    chk = False 
    x_s = max(x1, x_new1)
    x_e = min(x2, x_new2)
    if x_e >= x_s:
        chk = True 
    
    return x_s, x_e, chk

def solution1():
    fn = os.path.join(PATH, 'day22', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    x_coor = re.compile(r'x=(-?\d+)..(-?\d+)')
    y_coor = re.compile(r'y=(-?\d+)..(-?\d+)')
    z_coor = re.compile(r'z=(-?\d+)..(-?\d+)')
    
    res = set()
    for s in l.split('\n'):
        if s: 
            x = x_coor.findall(s)[0]
            y = y_coor.findall(s)[0]
            z = z_coor.findall(s)[0]
            for xx in range(max(-50, int(x[0])), min(50, int(x[1]) + 1)):
                for yy in range(max(-50, int(y[0])), min(50, int(y[1]) + 1)):
                    for zz in range(max(-50, int(z[0])), min(50, int(z[1]) + 1)):   
                        if s[:2] == 'on':
                            res.add((xx, yy, zz))
                        else:
                            if (xx, yy, zz) in res:
                                res.remove((xx, yy, zz))
    print(len(res))

def solution2():
    fn = os.path.join(PATH, 'day22', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    x_coor = re.compile(r'x=(-?\d+)..(-?\d+)')
    y_coor = re.compile(r'y=(-?\d+)..(-?\d+)')
    z_coor = re.compile(r'z=(-?\d+)..(-?\d+)')
    
    # can not use defualtdict(int)
    cnt = collections.Counter()
    for s in l.split('\n'):
        if s: 
            
            x = x_coor.findall(s)[0]
            y = y_coor.findall(s)[0]
            z = z_coor.findall(s)[0]
            
            if s[:2] == 'on':
                status = 1
            else:
                status = 0 
            
            new_bound = (int(x[0]), int(y[0]), int(z[0]), int(x[1]) + 1, int(y[1]) + 1, int(z[1]) + 1)

            new_coor_record = collections.Counter()
            
            if status == 1:
                new_coor_record[new_bound] += 1

            # the freq here denotes the range appearance in global scale, -1 means overlap one time, 1 means apear 1 time 
            for (xmin, ymin, zmin, xmax, ymax, zmax), freq in cnt.items():
                # shrink down the bound, 
                ## only check the overlap cases when 
                ## xmin  |_start  xmax |_end: mark the |_start to xmax part as overlap
                x_s, x_e, chk_x = chk_overlap(xmin, xmax, new_bound[0], new_bound[3])
                y_s, y_e, chk_y = chk_overlap(ymin, ymax, new_bound[1], new_bound[4])
                z_s, z_e, chk_z = chk_overlap(zmin, zmax, new_bound[2], new_bound[5])
                # if overlap, prevent double cnt, remove the overlapping part 
                if chk_x and chk_y and chk_z:
                    # if (x_s, y_s, z_s, x_e, y_e, z_e) not in new_coor_record:
                    #     print(new_coor_record[(x_s, y_s, z_s, x_e, y_e, z_e)])
                    new_coor_record[(x_s, y_s, z_s, x_e, y_e, z_e)] -= freq
            cnt.update(new_coor_record)

    
    res = 0

    for (x_s, y_s, z_s, x_e, y_e, z_e), freq in cnt.items():
        res += ((x_e - x_s) * (y_e - y_s) * (z_e - z_s) * (freq))

 
    print(res)


solution2()