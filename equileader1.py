#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:35:56 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    """
    N = len(A)
    if not (N >= 1 and N < 1e5):
        return 0
    if not (min(A) >= -1e9 and max(A) <= 1e9):
        return 0
    if N == 0:
        return 0
    if N == 1:
        return 0
    if N == 2:
        if A[0] != A[1]:
            return 0
        else:
            return 1

    nel = 0

    left_leaders = []
    leader = 0
    l = 0
    tally = [0]*(max(A)-min(A)+1)
    for i in range(N-1):
        tally[A[i]-min(A)] += 1
        if i == 0:
            leader = A[0]
            l += 1
        elif l > 0 and leader == A[i]:
            l += 1
        elif l > 0 and leader != A[i]:
            l -= 1
        elif l == 0:
            l += 1
            leader = A[i]
        else:
            pass

        if l and tally[leader-min(A)]>i/2:
            left_leaders.append([i, leader])

    right_leaders = []
    leader = 0
    l = 0
    tally = [0]*(max(A)-min(A)+1)
    for i in range(N-1, 0, -1):
#        print(i)
        tally[A[i]-min(A)]+=1
        if i==N-1:
            leader=A[N-1]
            l+=1
        elif l>0 and leader==A[i]:
            l+=1
        elif l>0 and leader!=A[i]:
            l-=1
        elif l==0:
            l+=1
            leader=A[i]
        else:
            pass

        if l and tally[leader-min(A)]>(N-i)/2:
            right_leaders.append([i-1, leader])

#    print(A)
#    print(left_leaders)
#    print(right_leaders)
    for ll in left_leaders:
        for rl in right_leaders:
            if ll==rl:
                nel+=1

    return nel

print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
print(solution([4, 3, 4, 4, 4, 2]))
print(solution([2, 2]))
print(solution([1, 2, 3, 4, 5]))
