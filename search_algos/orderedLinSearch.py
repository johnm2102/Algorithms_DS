#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sorted/Ordered List: 
    This is a sorted array so we do not need to scan the full thing
    Return -1 if it is larger than the desired integer
"""
#algorithm 
def orderedLinSearch(numList, val):
    for i in range(len(numList)):
        if numList[i] == val:
            return i
        elif numList[i] > val:
            return -1 
    return -1 

#test using array and result 
ar_1 = [1,2,3,4,5,6]

print(orderedLinSearch(ar_1, 3))
print(orderedLinSearch(ar_1, 500))



