#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
given an array of n numbers, come up with an algorithm that finds the elem that 
appears the most number of times in the array
"""
def maxRep(A):
    A.sort()
    j = 0 
    count = max = 1
    elem = A[0]
    for i in range(1,len(A)):
        if A[i] == elem:
            count += 1
            if count > max:
                max = count 
                maxRep = elem 
        else:
            count = 1
            elem = A[i]
    print(maxRep, "repeated for", max)
            

array1 = [1,2,4,4,5,6,8,3,2]
maxRep(array1)
