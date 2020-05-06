#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:12:40 2020

@author: artemponomarev
"""

def solution(N):
    # write your code in Python 3.6
    if not (1 <= N <= 1e9):
        return 0
    min_per=2*(N+1)
    factor = 1
    while factor * factor < N:
        # N has two factors: factor and N // factor
        if N % factor == 0:
            min_per=min(min_per, 2*(factor+N//factor))
        factor += 1
    # the last case is when N is square of some value.
    if factor * factor == N:
        min_per=min(min_per, 4*factor)
        
    return min_per

print(solution(30))
print(solution(100))
print(solution(101)) # prime N results in a rectangle with one side = 1
print(solution(pow(2, 8)))