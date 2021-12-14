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

def solution1():
    fn = os.path.join(PATH, 'day14', 'input.txt')
    l = read_txt(fn)
    lines = ''.join(l)
    temp, pairs = lines.split('\n\n')
    d = {}
    d_time = collections.defaultdict(int)
    for p in pairs.split('\n'):
        if p:
            k, v = p.split(' -> ')
            d[k] = v 

    for i in range(len(temp)-1):
        a = temp[i:i+2]
        d_time[a] += 1

    for _ in range(40):
        d_new = collections.defaultdict(int)
        for k_pair in d_time.keys():
            if k_pair in d:
                # insert 
                insert = d[k_pair]
                insert_left = k_pair[0] + insert
                insert_right = insert + k_pair[1] 
                
                d_new[insert_left] += d_time[k_pair]
                d_new[insert_right] += d_time[k_pair]

        d_time = d_new.copy() 

    # count letter {'NB': 2, 'BC': 2, 'CC': 1, 'CN': 1, 'BB': 2, 'CB': 2, 'BH': 1, 'HC': 1}) NBCCNBBBCBHCB   B*cnt + 1
    cnt = collections.defaultdict(int)
    for k_pair in d_time.keys():
        cnt[k_pair[0]] += d_time[k_pair]
    cnt[temp[-1]] += 1

    # count least and most common 
    max_x, min_x = -1, float('inf')
    for c in cnt.keys():
        max_x = max(cnt[c], max_x)
        min_x = min(cnt[c], min_x)
    
    print(max_x-min_x)

    #     for vv in k:
    #         if vv in cnt:
    #             cnt[vv] += v 
    #         else:
    #             cnt[vv] = v
    # print(cnt)
    #print(d)

def solution2():
    fn = os.path.join(PATH, 'day14', 'test.txt')
    l = read_txt(fn)



solution1()