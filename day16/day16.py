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

def read_txt(filename):
    with open(filename) as file:
        lines = file.readline()
    return lines 

def parse_packet(packet, idx):
    # version 
    v = packet[idx:idx+3]
    # type id 
    type_id = packet[idx+3:idx+6]
    return int(v, 2), int(type_id, 2)

def sub_packet_length(packet):
    # get a long packet and return the packet length
    # when packet is 4 
    idx = 0
    cnt = 0 
    packet_num = ''
    while True: 
        cnt += 1
        if packet[idx] == '0':
            packet_num += packet[idx+1:idx+5]
            break 
        if packet[idx] == '1':
            packet_num += packet[idx+1:idx+5]
            idx += 5

    return 5*cnt, int(packet_num, 2)

def parse_packet_recusive(packet, res, idx):
    v, type_id = parse_packet(packet, idx)
    res.append(v)
    idx += 6
    if type_id == 4:
        length,_ = sub_packet_length(packet[idx:])
        return idx + length
    else:
        type_len = packet[idx]
        idx += 1
        if type_len == '1':
            k = int(packet[idx:idx+11], 2)
            # 11 bits
            idx += 11
            #number of sub-packets immediately contained
            for _ in range(k):
                # print(idx)
                idx = parse_packet_recusive(packet, res, idx)
        if type_len == '0':
            # 15 bits 
            k = int(packet[idx:idx+15],2)
            idx += 15
            bound = idx + k
            # total length in bits of the sub-packets
            while idx < bound:
                # print(idx)
                idx = parse_packet_recusive(packet, res, idx)
        return idx


def sumpacket(sub):
    return sum(sub)

def product(sub):
    p = 1 
    for s in sub:
        p *= s
    return p 

def minumum(sub):
    return min(sub)

def maximum(sub):
    return max(sub)

def greater(sub):
    return 1 if sub[0] > sub[1] else 0

def less(sub):
    return 1 if sub[0] < sub[1] else 0

def equal(sub):
    return 1 if sub[0] == sub[1] else 0

SWITCH = {
        0: sumpacket,
        1: product,
        2: minumum,
        3: maximum,
        5: greater,
        6: less,
        7: equal}

def parse_packet_recusive_v2(packet, res, idx):
    v, type_id = parse_packet(packet, idx)
    res.append(v)
    idx += 6
    if type_id == 4:
        length, packet_num = sub_packet_length(packet[idx:])
        return idx + length, packet_num
    else:
        type_len = packet[idx]
        idx += 1
        sub_packets = []
        if type_len == '1':
            k = int(packet[idx:idx+11], 2)
            # 11 bits
            idx += 11
            #number of sub-packets immediately contained
            for _ in range(k):
                idx, value = parse_packet_recusive_v2(packet, res, idx)
                sub_packets.append(value)
        if type_len == '0':
            # 15 bits 
            k = int(packet[idx:idx+15],2)
            idx += 15
            bound = idx + k
            # total length in bits of the sub-packets
            while idx < bound:
                idx, value = parse_packet_recusive_v2(packet, res, idx)
                sub_packets.append(value)

        # Get the type id  from switcher dictionary
        print(sub_packets)
        func = SWITCH.get(type_id)
        value = func(sub_packets)
        return idx, value 
    
def solution1():
    fn = os.path.join(PATH, 'day16', 'input.txt')

    l = read_txt(fn)
    hex_l = [f'{int(x,16):04b}' for x in l if x != '\n']
    packet = ''.join(hex_l)

    res = [] 
    parse_packet_recusive(packet, res, 0)
    print(sum(res))

def solution2():
    fn = os.path.join(PATH, 'day16', 'input.txt')
    
    l = read_txt(fn)
    hex_l = [f'{int(x,16):04b}' for x in l if x != '\n']
    packet = ''.join(hex_l)

    res = [] 
    idx, v = parse_packet_recusive_v2(packet, res, 0)
    print(v)
   
solution2()     