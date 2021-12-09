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
    fn = os.path.join(PATH, 'day09', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    brd = [[0]]

    # four direction 
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 0
    m,n = len(lines), len(lines[0])

    for i in range(m):
        for j in range(n):
            for k in range(4):
                x1 = i + dir[k][0]
                y1 = j + dir[k][1]
                if x1 < m and x1 >=0 and y1 >=0 and y1 < n:
                    if int(lines[i][j]) >= int(lines[x1][y1]):
                        #print(lines[i][j])
                        break
        
                if k == 3:
                    print(i, j, int(lines[i][j]))
                    res += int(lines[i][j]) + 1
    print(res)

def solution2():
    fn = os.path.join(PATH, 'day09', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    brd = [[0]]
    print(lines)
    # four direction 
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 0
    m,n = len(lines), len(lines[0])

    visited = set()

    def dfs(x, y, path):
    # search for basins
        if (x, y) in visited or int(lines[x][y]) == 9:
            return 
        visited.add((x, y))
        if int(lines[x][y]) != 9:
            path.append(int(lines[x][y]))

        for k in range(4):
            x1 = x + dir[k][0]
            y1 = y + dir[k][1]
            if 0 <= x1 < m and 0 <= y1 < n:
                dfs(x1, y1, path)

    ans = []
    for i in range(m):
        for j in range(n):
            visited = set()
            res = []
            dfs(i, j, res)
            res.sort()
            if res not in ans and res:
                ans.append(res)
    
    final = [len(x) for x in ans]
    final.sort()
    print(final[-1]*final[-2]*final[-3])
    
  
solution2()