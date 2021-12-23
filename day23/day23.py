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


def solution1():
    fn = os.path.join(PATH, 'day23', 'test.txt')
    l = read_txt(fn)
    lines = [line.rstrip() for line in l]
    dir = [0, -1, 0, 1, 0]

    #############
    #AA.........#
    ###B#.#.#D###
      #D#B#C#C#
      #########
               
    # A 5
    # A 6 
    # B 5    
    # C 6 
    # B 3    
    # B 4     
    # D 2    
    # C 5  
    # D 10 
    # D 2
    # A 3 
    # A 3 
    print(5+6+50+600+30+40+2000+500+10000+2000+3+3)

def solution2():
    fn = os.path.join(PATH, 'day23', 'test.txt')
    l = read_txt(fn)
    lines = [line.rstrip() for line in l]

      
    #############
    #AA.......AA#
    ###.#B#.#D###
      #.#B#.#D#
      #.#B#C#D#
      #.#B#C#D#
      #########


  #############
  #...........#
  ###A#B#C#D###
    #A#B#C#D#
    #A#B#C#D#
    #A#B#C#D#
    #########

    # A <- 5     5      
    # A <- 6     6
    # B <- 6     60
    # A <- 5     5
    # B -> 6     60
    # C -> 8     800
    # B <- 4     40
    # C -> 9     900
    # B -> 5     50
    # B -> 5     50
    # B -> 5     50
    # B <- 4     40
    # A -> 3     3
    # D <- 4     4000
    # A -> 3     3
    # C <- 7     700
    # C <- 7     700
    # A <- 2     2
    # D -> 7     7000
    # A -> 3     3
    # A -> 4     4
    # D -> 11    11000
    # D -> 11    11000
    # D -> 11    11000
    # A -> 5     5
    # A -> 5     5
    # A <- 9     9
    # A <- 9     9
    print(5+6+60+5+60+800+40+900+50+50+50+40+3+4000+3+700+700+2+7000+3+4+11000*3+10+18)

solution2()