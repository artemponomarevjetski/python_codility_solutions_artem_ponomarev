#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:33:35 2020

@author: artemponomarev
"""

def solution(A): # 53%
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    max double slice
    """
    N = len(A)
    if not (N >= 3 and N < 1e5):
        return 0
    if not (min(A) >= -1e4 and max(A) <= 1e4):
        return 0

    global_max = sum1 = 0
    stack = []
    for i in range(1, N-1):
        if i == 1:
            global_max = 0
            sum1 = A[i]
            stack.append(A[i])
        else:
            if A[i] < A[i]+sum1:
                stack.append(A[i])
                sum1 += A[i]
                for j in range(len(stack)):
                    sum3 = sum1-stack[j]
                    if sum3 > global_max:
                        global_max = sum3
#                print(A, i, A[i], sum1, stack, global_max)
            else:
                stack = []
                stack.append(A[i])
                sum1 = A[i]

    return global_max

print(solution([4, 3, 4, 4, 4, 2]))
print(solution([2, 2]))
print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
print(solution([1, 2, 300, 4, 5]))

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
print(solution([5, 17, 0, 3]))
