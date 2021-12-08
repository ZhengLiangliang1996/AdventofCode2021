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
    fn = os.path.join(PATH, 'day08', 'test.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    # 1->2
    # 4->4
    # 7->3
    # 8->7
    res = 0
    for i in lines:
        a,b = i.split(' | ')
        a = a.split(' ')
        b = b.split(' ')
        l = []
        l_cnt = []
        for j in a:
            sub = list(set(j))
            sub.sort()
            l.append(sub)

        for j in b:
            print(j)
            k = list(set(j))
            
            k.sort()
            if len(k)== 2 or len(k) == 4 or len(k) == 3 or len(k) == 7:
                res += 1
    print(res)


def solution2():
    fn = os.path.join(PATH, 'day08', 'test.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    
    res = 0
    for i in lines:
        a,b = i.split(' | ')
        a = a.split(' ')
        b = b.split(' ')
        l = []
        l_len = []
        
        for j in a:
            l.append(set(j))
            l_len.append(len(j))
        
        # 1->2 ab 
        # 4->4 eafb
        # 7->3 dab
        # 8->7 acedgfb

        # acedgfb: 8
        # cdfbe: 5
        # gcdfa: 2
        # fbcad: 3
        # dab: 7
        # cefabd: 9
        # cdfgeb: 6
        # eafb: 4
        # cagedb: 0
        # ab: 1
        l_1_idx = l_len.index(2)
        l_4_idx = l_len.index(4)
        l_7_idx = l_len.index(3)
        l_8_idx = l_len.index(7)
        set_1, set_4, set_7, set_8 = l[l_1_idx], l[l_4_idx], l[l_7_idx], l[l_8_idx]
        
        all_set_len_6, all_set_len_5 = [], []
        for i in range(len(l_len)):
            if l_len[i] == 6:
                all_set_len_6.append(l[i])
            if l_len[i] == 5:
                all_set_len_5.append(l[i])
        set_0, set_6, set_9 = None, None, None

        # distignuish  9 6 0
        for s in all_set_len_6:
            # 4 is the subset of 9 
            if set_4.issubset(s):
                set_9 = s
        for s in all_set_len_6:
            if s != set_9 and set_7.issubset(s):
                set_0 = s 
        # rest is set 6 
        set_6 = [s for s in all_set_len_6 if s not in [set_9, set_0]][0]
            
        # distignuish  5, 2, 3
        # set_7 + set_5 = set_9
        set_5, set_2, set_3 = None, None, None 
        # print(set_7.union(set_4))
        for s in all_set_len_5:
            
            union_9 = set.union(set_1, s)
            if union_9 == set_9:
                set_5 = s
            if set_1.issubset(s):
                set_3 = s
        # rest is set 9
        set_2 = [s for s in all_set_len_5 if s not in [set_5, set_3]][0]

        set_all = [set_0, set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9]
        num = ''
        
        for j in b:
            num += str(set_all.index(set(j)))
        
        res += int(num)
        print(int(num))

    print(res)
solution2()