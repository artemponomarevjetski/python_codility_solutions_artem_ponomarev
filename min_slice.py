#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:37:25 2020

@author: artemponomarev
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [4, 2, 2, 5, 1, 5, 8]

def solution(A):
    # write your code in Python 3.6
    """
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 2 and N <= 1e5):
        return 0
    if not (min(A) >= -1e4 and max(A) <= 1e4):
        return 0
    P = 0
    Q = 1
    cur_aver = 0
    min_aver = 1e4+1
    Pmin = 0
    for i in range(N-1):
        P = i
        Q = P+1
        cur_aver = (A[Q]+A[P])/(i+1-i+1)
        if cur_aver < min_aver:
            min_aver = cur_aver
            Pmin = P
        if  Q < N-1:
            for j in range(i+2, N):
                Q = j
                if A[Q] < cur_aver:
                    cur_aver = (A[Q]+cur_aver*(j-i))/(j-i+1)
                    if cur_aver < min_aver:
                        min_aver = cur_aver
                        Pmin = P
                else:
                    break

    return Pmin

# main()
print("result  = ", solution(A))

#
#    Task description
#A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
#
#For example, array A such that:
#
#    A[0] = 4
#    A[1] = 2
#    A[2] = 2
#    A[3] = 5
#    A[4] = 1
#    A[5] = 5
#    A[6] = 8
#contains the following example slices:
#
#slice (1, 2), whose average is (2 + 2) / 2 = 2;
#slice (3, 4), whose average is (5 + 1) / 2 = 3;
#slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
#The goal is to find the starting position of a slice whose average is minimal.
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
#
#For example, given array A such that:
#
#    A[0] = 4
#    A[1] = 2
#    A[2] = 2
#    A[3] = 5
#    A[4] = 1
#    A[5] = 5
#    A[6] = 8
#the function should return 1, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [2..100,000];
#each element of array A is an integer within the range [−10,000..10,000].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ double_quadruple
#two or four elements ✔OK
#▶ simple1
#simple test, the best slice has length 3 ✔OK
#▶ simple2
#simple test, the best slice has length 3 ✔OK
#▶ small_random
#random, length = 100 ✔OK
#▶ medium_range
#increasing, decreasing (legth = ~100) and small functional ✔OK
#expand allPerformance tests
#▶ medium_random
#random, N = ~700 ✔OK
#▶ large_ones
#numbers from -1 to 1, N = ~100,000 ✔OK
#▶ large_random
#random, N = ~100,000 ✔OK
#▶ extreme_values
#all maximal values, N = ~100,000 ✔OK
#▶ large_sequence
#many seqeneces, N = ~100,000 ✔OK
