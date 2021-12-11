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

def count_flash(brd):
    cnt = 0
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                cnt += 1
    return cnt 

def solution1():
    fn = os.path.join(PATH, 'day11', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    m, n = len(lines), len(lines[0])
    brd = [[int(lines[i][j]) for j in range(n)] for i in range(m)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    res = 0

    def dfs(x, y, brd, flashed):
    # search for flashes
        if (x, y) in flashed:
            return 

        flashed.add((x, y))

        for k in range(8):
            x1 = x + dir[k][0]
            y1 = y + dir[k][1]

            if 0 <= x1 < m and 0 <= y1 < n:
                brd[x1][y1] += 1
                if brd[x1][y1] > 9:
                    dfs(x1, y1, brd, flashed)

    for s in range(100):
        # increase by 1 
        brd = [[brd[i][j] + 1 for j in range(n)] for i in range(m)]
        flashed = set()
        for i in range(m):
            for j in range(n):
                # flash
                if brd[i][j] > 9:
                    dfs(i, j, brd, flashed)

        for x, y in flashed:
            brd[x][y] = 0

        res += count_flash(brd)

    print(res)


def solution2():
    fn = os.path.join(PATH, 'day11', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    m, n = len(lines), len(lines[0])
    brd = [[int(lines[i][j]) for j in range(n)] for i in range(m)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    res = 0

    def dfs(x, y, brd, flashed):
    # search for flashes
        if (x, y) in flashed:
            return 

        flashed.add((x, y))

        for k in range(8):
            x1 = x + dir[k][0]
            y1 = y + dir[k][1]

            if 0 <= x1 < m and 0 <= y1 < n:
                brd[x1][y1] += 1
                if brd[x1][y1] > 9:
                    dfs(x1, y1, brd, flashed)
    sync = False 
    cnt = 0
    while True:
        if sync:
            break 
        # increase by 1 
        brd = [[brd[i][j] + 1 for j in range(n)] for i in range(m)]
        flashed = set()
        for i in range(m):
            for j in range(n):
                # flash
                if brd[i][j] > 9:
                    dfs(i, j, brd, flashed)
        
        for x, y in flashed:
            brd[x][y] = 0

        if count_flash(brd) == m*n:
            sync = True

        cnt += 1

    print(cnt)



solution2()