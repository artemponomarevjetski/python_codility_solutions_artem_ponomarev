#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:41:20 2020

@author: artemponomarev
"""

def solution(N):
    """
    number of divisors
    """
    if not (N >= 1 and N <= 2147483647):
        return 0
    if N < -1:
        return 0
    if N == 0:
        return 0
    if N == 1:
        return 1
    count = 1
    for i in range(1, int(N / 2) + 1):
        if N % i == 0:
            count += 1
    return count

print(solution(20))
