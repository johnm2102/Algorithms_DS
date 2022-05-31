#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- Given an array of n numbers, give an algorithm for checking whether there are 
    any duplicate elements in the array or no?
"""
def checkDuplicates(A):
    A.sort()
    for i in range(0, len(A)-1):
        for j in range(i + 1, len(A)):
            if A[i] == A[j]: 
                print("There are duplicates: ", A[i])
                return; 
    print("There are no duplicates")
            
    

Ar1 = [3,2,3,20,22,32]
checkDuplicates(Ar1)
