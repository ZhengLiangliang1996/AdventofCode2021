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
    fn = os.path.join(PATH, 'day10', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    d = {')':3, ']':57, '}':1197, '>':25137}
    res_dict = {')':0, ']':0, '}':0, '>':0}
    map1 = {'(':')', '[':']', '{':'}', '<':'>'}
    for l in lines:
        s = []
        print(l)
        for j in l:
            if j in ['(', '[', '{', '<']:
                s.append(j)
                continue
            elif j in [')', ']', '}', '>']:
                if len(s) == 0:
                    res_dict[j] += 1
                    break 
                else:
                    a = s.pop()
                    if map1[a] != j:
                        print(a, j)
                        res_dict[j] += 1
                        break
                
    print(res_dict)
    res = 0
    for k in res_dict.keys():
        res += res_dict[k] * d[k]
    print(res)



def solution2():
    fn = os.path.join(PATH, 'day10', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    d = {')':1, ']':2, '}':3, '>':4}
    res_dict = {')':0, ']':0, '}':0, '>':0}
    map1 = {'(':')', '[':']', '{':'}', '<':'>'}
    remain = []
    for l in lines:
        s = []
        cnt = 0
        for j in l:
            cnt += 1
            if j in ['(', '[', '{', '<']:
                s.append(j)
                continue
            elif j in [')', ']', '}', '>']:
                if len(s) == 0:
                    res_dict[j] += 1
                    break 
                else:
                    a = s.pop()
                    if map1[a] != j:
                        res_dict[j] += 1
                        break
        
        if cnt == len(l):
            remain.append(l)

    # determin the remaining score 
    res = []
    for l in remain:
        s = []
        cnt = 0
        for j in l:
            if j in ['(', '[', '{', '<']:
                s.append(j)
                continue
            elif j in [')', ']', '}', '>']:
                s.pop()
        for k in s[::-1]:
            cnt = cnt * 5 + d[map1[k]]
        res.append(cnt)
    res.sort()
    print(res[len(res)//2])
  
solution2()