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
    fn = os.path.join(PATH, 'day12', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    res = []
    brd = collections.defaultdict(list)
    for x in lines:
        s, e = x.split('-')
        brd[s].append(e)
        brd[e].append(s)
    # traverse brd 
    # dfs with backtrack 
    def dfs(node, path):
        if node == 'end':
            res.append(path)
            return 
        # only lower case can visited at most once
        if not node.isupper() and node != 'start':
            visited.add(node)

        # search for neighbour
        for ngh in brd[node]:
            if ngh == 'start': continue 
            if ngh not in visited:
                dfs(ngh, path + [ngh])

        if not node.isupper() and node != 'start':
            visited.remove(node)

    visited = set('start')   
    dfs('start', ['start'])
    print(res)
    print(len(res)) 

def solution2_1():
    fn = os.path.join(PATH, 'day12', 'input.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    res = []
    brd = collections.defaultdict(list)
    for x in lines:
        s, e = x.split('-')
        brd[s].append(e)
        brd[e].append(s)
    # traverse brd 
    # dfs with backtrack 
    
    def dfs(node, path, visited):
        if node == 'end':
            res.append(path)
            return 
        
        if not node.isupper() and node != 'start':
            visited += [node]

        # search for neighbour
        for ngh in brd[node]:
            if ngh == 'start': continue 
            # lower case can visited at most 2 once
            if ngh not in visited or len(visited) <= len(set(visited)):
                dfs(ngh, path + [ngh], visited)

        if not node.isupper() and node != 'start':
            visited.remove(node)

    visited = ['start']
    dfs('start', ['start'], visited)
    print(res)
    print(len(res)) 

# TLE
def solution2():
    fn = os.path.join(PATH, 'day12', 'test.txt')
    l = read_txt(fn)
    lines = [x.replace('\n', '') for x in l]
    res = []
    brd = collections.defaultdict(set)
    visited = {}
    for x in lines:
        s, e = x.split('-')
        brd[s].add(e)
        brd[e].add(s)
        visited[s] = 0
        visited[e] = 0
    # traverse brd 
    # dfs with backtrack 
    def dfs(node, path):
        if node == 'end' and path not in res:
            res.append(path)
            return 
        # only lower case can visited at most once
        if not node.isupper() and node != 'start':
            visited[node] += 1
            # all the remaining could be 2 
        # search for neighbour
        for ngh in brd[node]:
            if ngh == 'start': continue 
            if 0 <= visited[ngh] < 2:
                dfs(ngh, path + [ngh])

        if not node.isupper() and node != 'start':
            visited[node] -= 1


    dfs('start', ['start'])
    ans = 0
    brd_time = {}

    for r in res:
        small = 0
        for b in brd.keys():
            if not b.isupper():
                brd_time[b] = 0

        for r_sub in r:
            if not r_sub.isupper():
                brd_time[r_sub] += 1
        print(brd_time)
        for v in brd_time.keys():
            if brd_time[v] >= 2:
                small += 1

        if small <= 1:
            ans += 1

    print(ans)

solution2_1()