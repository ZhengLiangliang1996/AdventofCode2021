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
import copy
PATH = '/Users/liangliang/Desktop/AdventofCode2021'

def read_txt(filename):
    with open(filename) as file:
        lines = file.readlines()
       
    return lines 

def padding(image, padding_size=2, padding_value=0):
    m,n = image.shape
    if padding_value == 0:
        padding_array = np.zeros([m + 2 * padding_size, n + 2 * padding_size])
    if padding_value == 1:
        padding_array = np.ones([m + 2 * padding_size, n + 2 * padding_size])
    padding_array[padding_size:m+padding_size, padding_size:n + padding_size] = image
    return padding_array

def enhance(small, ref):
    a = ''
    for i in range(len(small)):
        for j in range(len(small[0])):
            a += str(int(small[i][j]))
    
    a_bin = int(a, 2)

    return ref[a_bin]

def transform(image, pad_image, ref):
    for i in range(1, len(image)-1):
        for j in range(1, len(image[0])-1):
            small = image[i-1:i+2,j-1:j+2]
            r = enhance(small, ref)   
            pad_image[i][j] = r
    return pad_image
    
    #return new_image

def run(image,ref,padding_value):
    m,n = image.shape
    image_pad = np.zeros([m, n]) 
    # stt with padding 0
    image = padding(image, padding_size=2, padding_value=padding_value)

    padding_value = ref[0] if padding_value == 0 else ref[-1]
    # 
    image_pad = padding(image_pad, padding_size=2, padding_value=padding_value)

    image_pad = transform(image, image_pad, ref)

    return image_pad

def solution1():
    fn = os.path.join(PATH, 'day20', 'input.txt')
    l = read_txt(fn)
    l = ''.join(l)
    a = l.split('\n\n')
    
    ref = a[0]
    ref_map = {'.':0,'#':1}
    ref = [ref_map[x] for x in ref if x != '\n' and x]

    image = []
    for sub in a[1].split('\n'):
        sub_list = [] 
        if sub: 
            for s in sub: 
                if s == '.':
                    sub_list.append(0)
                if s == '#':
                    sub_list.append(1)
        if sub_list:
            image.append(sub_list)
    
    image = np.array(image)
    # padding_size = 2 
    padding_value = 0
    
    for i in range(2):
        image = run(image,ref,padding_value)
        
        if padding_value == 0:
            padding_value = ref[0]
        else:
            padding_value = ref[-1]
    
    sum_all = 0
    print(np.sum(image))


solution1()