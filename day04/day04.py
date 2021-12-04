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
import numpy as np

PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()

    return lines 

def chk(mrk):
    # check row 
    brd = [[0 for i in range(5)] for j in range(5)]
    brd = np.array(brd)
    FND = False 
    for i in mrk:
        if FND:
            break
        row = i//5
        col = i%5
        brd[row][col] = 1

        for a in np.sum(brd, axis=0):
            if a == 5:
                FND = True
                break
        for a in np.sum(brd, axis=1):
            if a == 5:
                FND = True
                break
    if FND:
        print(brd)
    return FND

def solution1():
    fn = os.path.join(PATH, 'day04', 'input.txt')
    lines = read_txt(fn)
    lines = ''.join(lines)
    lines = lines.split('\n\n')
    lines = [line.replace('\n', ' ').replace('  ', ' ').strip() for line in lines]
    drw = lines[0]
    drw = [x for x in drw.split(',')]
    
    brd = collections.defaultdict(list)

    res = 0
    a = []
    board = [x.split(' ') for x in lines[1:]]
    won_boards = []
    CHECK = False
    #search winner 
    for d in drw:
        # mark in brd 
        if CHECK:
            break
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == d:
                    brd[i].append(j)
        
        for i in range(len(board)):
            # found winner
            if chk(brd[i]):
                if len(won_boards) == len(board):
                    for j in range(25):
                        if j not in brd[won_boards[-1]]:
                            a.append(j)
                    a = sum([int(board[won_boards[-1]][x]) for x in a])
                    res = a*int(d)
                    print(res)
                    CHECK = True
                    break
                if i not in won_boards:
                    won_boards.append(i)
                

solution1()
