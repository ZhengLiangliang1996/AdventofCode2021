#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import collections
import os
import re
import numpy as np

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

def rotate(points, orient):
    # YZ change 
    # 24 different orientations: facing positive or negative x, y, or z, and considering any of four directions "up" from that facing.
    # https://en.wikipedia.org/wiki/Right-hand_rule
    # TODO: implement using degree
    x, y, z = points
    rot= {0:[x,y,z],1:[-x,-y,z],2:[-x,y,-z],3:[x,-y,-z],4:[y,z,x],5:[-y,-z,x],6:[-y,z,-x],
        7:[y,-z,-x],8:[z,x,y],9:[-z,-x,y],10:[-z,x,-y], 11:[z,-x,-y], 12:[-x,z,y],
        13:[x,-z,y], 14:[x,z,-y], 15:[-x,-z,-y], 16:[-y,x,z], 17:[y,-x,z], 18:[y,x,-z],
        19:[-y,-x,-z],20:[-z,y,x], 21:[z,-y,x],22:[z,y,-x],23:[-z,-y,-x]}
    
    return tuple(rot[orient])

def get_same_direction(nm):
    res = []
    for i in range(24):
        d = set()
        for nm_sub in nm:
            d.add(rotate(nm_sub, i))
        res.append(d)
    return res 

def solution1():
    fn = os.path.join(PATH, 'day19', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    a = l.split('\n\n')
    becons = []

    for s in a: 
        each_s = set()
        for coor in s.split('\n'):
            if coor and not coor.startswith('---'): 
                x, y, z = [int(x) for x in coor.split(',')]
                each_s.add((x, y, z))
        becons.append(each_s)
    
    match_set = becons[0].copy()
    not_match_set = becons[1:]
    #FOUND = False
    while not_match_set:
        for m in list(match_set):
            for nm in list(not_match_set):
                rot_all = get_same_direction(nm)
                for i in range(24):
                    Found = False
                    # possible_m_all = set()
                    for r in rot_all[i]:   
                        if Found: break
                        # if 2 are the same becon, 
                        # d = m - nm
                        dx = m[0] - r[0]
                        dy = m[1] - r[1]
                        dz = m[2] - r[2]
                        # nm + d == m
                        possible_m_all = set()
                        for x,y,z in rot_all[i]:
                            possible_m_all.add((x+dx, y+dy, z+dz))
                        if len(possible_m_all.intersection(match_set)) >= 12:
                            print('found')
                            match_set.update(possible_m_all)
                            not_match_set.remove(nm)
                            Found = True 
    
    print(len(match_set))

def solution2():
    fn = os.path.join(PATH, 'day19', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    a = l.split('\n\n')
    becons = []

    for s in a: 
        each_s = set()
        for coor in s.split('\n'):
            if coor and not coor.startswith('---'): 
                x, y, z = [int(x) for x in coor.split(',')]
                each_s.add((x, y, z))
        becons.append(each_s)
    
    match_set = becons[0].copy()
    not_match_set = becons[1:]
    #FOUND = False
    scanners_coor = []
    while not_match_set:
        for m in list(match_set):
            for nm in list(not_match_set):
                rot_all = get_same_direction(nm)
                for i in range(24):
                    Found = False
                    # possible_m_all = set()
                    for r in rot_all[i]:   
                        if Found: break
                        # if 2 are the same becon, 
                        # d = m - nm
                        dx = m[0] - r[0]
                        dy = m[1] - r[1]
                        dz = m[2] - r[2]
                        # nm + d == m
                        possible_m_all = set()
                        for x,y,z in rot_all[i]:
                            possible_m_all.add((x+dx, y+dy, z+dz))
                        if len(possible_m_all.intersection(match_set)) >= 12:
                            print('Found')
                            scanners_coor.append([dx, dy, dz])
                            match_set.update(possible_m_all)
                            not_match_set.remove(nm)
                            Found = True 
    
    # print(len(match_set))
    scanner0 = [0, 0, 0]
    scanners_coor = [scanner0] + scanners_coor
    max_a = -1 
    for i in range(len(scanners_coor)):
        for j in range(len(scanners_coor)):
            if i != j:
                d = abs(scanners_coor[i][0] - scanners_coor[j][0]) + \
                    abs(scanners_coor[i][1] - scanners_coor[j][1]) + \
                    abs(scanners_coor[i][2] - scanners_coor[j][2])
                max_a = max(d, max_a)
    
    print(max_a)
solution2()