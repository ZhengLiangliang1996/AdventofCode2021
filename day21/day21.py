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

def rolls(cnt):
    sum_three = 0
    for _ in range(3):
        sum_three += cnt 
        cnt += 1
    return sum_three, cnt

def solution1():
    fn = os.path.join(PATH, 'day21', 'input.txt')
    # l = read_txt(fn)
    # l = ''.join(l)
    # a = l.split('\n\n')
    p1 = [7, 0]
    p2 = [6, 0]
    roll = 1
    FOUND = True 
    while FOUND: 
        for p in range(2):
            if p == 0:
                # player 1
                temp = (p1[0] + ((3*roll) + 3 - 1)) % 10 + 1
                roll += 3 
                p1[1] += temp
                p1[0] = temp
                if p1[1] >= 1000: 
                    print(p2[1] * (roll - 1))
                    FOUND = False 
                    break
                # print(p1, temp)
            else: 
                temp = (p2[0] + ((3*roll) + 3 - 1)) % 10 + 1
                roll += 3 
                p2[1] += temp
                p2[0] = temp
                if p2[1] >= 1000: 
                    print(p1[1] * (roll - 1))
                    FOUND = False 
                    break
                # print(p2)
    

def solution2():
    fn = os.path.join(PATH, 'day21', 'input.txt')
    # l = read_txt(fn)
    # l = ''.join(l)
    # a = l.split('\n\n')
    p1_pos, p1_s = 7, 0
    p2_pos, p2_s = 6, 0
    # roll = 1
    # TLE
    # cannot use list becasue its not hasable
    #@functools.lru_cache()
    # def universe_roll(p1_pos, p2_pos, p1_s, p2_s, p):
    #     universe_p1, universe_p2 = 0, 0

    #     for i in (1,2,3):
    #         for j in (1,2,3):
    #             for k in (1,2,3):
    #                 if p == 0: # p1 
    #                     temp = (p1_pos + i + j + k - 1) % 10 + 1
    #                     p1_s_new = p1_s + temp
    #                     # p1_pos_new = temp
    #                     if p1_s_new >= 21: 
    #                         universe_p1 += 1
    #                     else: 
    #                         u1, u2 = universe_roll(temp, p2_pos, p1_s_new, p2_s, 1)
    #                         universe_p1 += u1 
    #                         universe_p2 += u2
    #                 else:
    #                     temp = (p2_pos + i + j + k - 1) % 10 + 1
    #                     p2_s_new = p2_s + temp
    #                     # p2_pos_new = temp
    #                     if p2_s_new >= 21: 
    #                         universe_p2 += 1
    #                     else: 
    #                         u1, u2 = universe_roll(p1_pos, temp, p1_s, p2_s_new, 0)
    #                         universe_p1 += u1 
    #                         universe_p2 += u2
        
    #     return universe_p1, universe_p2

    # dp with mem
    # with corresponding pos1, pos2 and score1 and score 2: th winning time tuple
    dp = {} 
    def dp_cnt(p1_pos, p2_pos, p1_s, p2_s):
        # base case 
        if p1_s >= 21:
             return (1, 0)
        if p2_s >= 21:
            return (0, 1)
        # memorization 
        if (p1_pos, p2_pos, p1_s, p2_s) in dp: 
            return dp[(p1_pos, p2_pos, p1_s, p2_s)]
        res = (0, 0) 
        for i in (1,2,3):
            for j in (1,2,3):
                for k in (1,2,3):
                    # if p == 0: # p1 
                    p1_pos_new = (p1_pos + i + j + k - 1) % 10 + 1
                    p1_s_new = p1_s + p1_pos_new
                    u1, u2 = dp_cnt(p2_pos, p1_pos_new, p2_s, p1_s_new)

                    res = (res[0] + u2, res[1] + u1)
        dp[(p1_pos, p2_pos, p1_s, p2_s)] = res
        return res
    
    print(dp_cnt(p1_pos, p2_pos, p1_s, p2_s))

 
solution2()