#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Search: 
    Most common kind of search problem known 
    Splits array into half, then determines which half to look at based on 
    size of value 
    remember:
        mid = (lo + hi)/ 2 
"""
#algo for iterative 
def binSearchIter(numList, val):
    lo = 0
    hi = len(numList) - 1
    while lo <= hi:
        mid = (lo + hi)//2 
        if numList[mid] < val: 
            lo = mid + 1
        elif numList[mid] > val:
            hi = mid - 1
        else:
            return mid 
    return -1 
        
    

#Array 
A = [1, 23, 42, 49, 86, 492, 582]

#search 
print(binSearchIter(A, 582))
print(binSearchIter(A, 123))