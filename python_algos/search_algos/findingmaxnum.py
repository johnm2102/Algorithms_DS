#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
given an array of n numbers, come up with an algorithm that finds the elem that 
appears the most number of times in the array
"""       
def findLargest(arr): 
    largest = arr[len(arr) - 1]
    for i in range(1, len(arr)):
        if arr[i] > largest: 
            largest = arr[i]
    return largest

arr = [1, 5,6, 199, 4, 3, 8]

print(findLargest(arr))





