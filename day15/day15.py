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
import heapq 

PATH = '/Users/liangliang/Desktop/AdventofCode2021'
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

# refer to https://zhuanlan.zhihu.com/p/259401289
def dijkstra(start, target, graph):
    visited = set()
    q = [(0, start)]
    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if curr_node == target:
            return curr_dist
        
        if curr_node in visited: continue  
        visited.add(curr_node)

        for ngh_node, ngh_dist in graph[curr_node]:
            new_d = curr_dist + ngh_dist
            heapq.heappush(q, (new_d, ngh_node))
    return -1

def neighbirs(x, y, m, n, brd):
    # return neighbir and node dist 
    res = [] 
    for d in dir:
        x1 = x + d[0]
        y1 = y + d[1]
        if 0<= x1 < m and 0 <= y1 <n:
            res.append(((x1, y1), brd[x1][y1]))

    return res 

def solution1():
    fn = os.path.join(PATH, 'day15', 'test.txt')
    l = read_txt(fn)
    lines = ''.join(l)
    # build brd 
    brd_0 = [i for i in lines.split('\n') if i]
    brd = []
    for b in brd_0:
        res = []
        for i in b:
            res.append(int(i))
        brd.append(res)

    m, n = len(brd), len(brd[0])

    # ONLY WORK IN TEST CASE  
    # def dfs(brd, x, y):
    #     # success base case 
    #     if x == 0 and y == 0: return int(brd[x][y])
    #     if x < 0 or y < 0: return float('inf')

    #     if s[x][y] > 0: return s[x][y]

    #     res = brd[x][y] + min(dfs(brd, x-1, y), dfs(brd, x, y-1))
    #     s[x][y] = res 
    #     return s[x][y]

    # res = dfs(brd, m-1, n-1)
    # print(res-brd[0][0])
    print(m, n)
    # graph[node] = [node, dist]
    graph = {} 
    for i in range(m):
        for j in range(n):
            node = i, j 
            graph[node] = [(x, d) for (x, d) in neighbirs(i, j, m, n, brd)]
    #print(graph)
    dist = dijkstra((0, 0), (m-1, n-1), graph)
    print(dist)
    
    
def solution2():
    fn = os.path.join(PATH, 'day15', 'input.txt')
    l = read_txt(fn)
    lines = ''.join(l)
    # build brd 
    brd_0 = [i for i in lines.split('\n') if i]
    brd = []
    for b in brd_0:
        res = []
        for i in b:
            res.append(int(i))
        brd.append(res)
    m, n = len(brd), len(brd[0])

    brd_BIG = [[0 for _ in range(n*5)] for _ in range(m*5)]
    
    for i in range(5):
        for j in range(5):
            x_right = m * i
            y_down = n * j
            for b_i in range(m):
                for b_j in range(n):
                    big_x, big_y = b_i + x_right, b_j + y_down 
                    brd_BIG[big_x][big_y] = (brd[b_i][b_j] + x_right + y_down - 1) % 9 + 1
    # print(brd_BIG)
    # graph[node] = [node, dist]
    graph = {} 
    for i in range(m*5):
        for j in range(n*5):
            node = i, j 
            graph[node] = [(x, d) for (x, d) in neighbirs(i, j, m*5, n*5, brd_BIG)]
    #print(graph)
    dist = dijkstra((0, 0), (m*5-1, n*5-1), graph)
    print(dist)
    




solution2()