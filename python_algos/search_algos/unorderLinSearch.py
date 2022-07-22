#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unordered linear search:
    this is a type of search where we are given an array where the order of 
    elements are not known.
    its a pretty rough search algo because you have to scan the whole array to 
    see if the element is there or not 
"""
#unordered lin search function
def unOrderLinSearch(numList, val):
    for i in range(len(numList)):
        if numList[i] == val:
            #return print("Found value in index : %i" %i)
            return i 
    #return print("Did not find value in index")
    return -1
    
#example 
A = [1,3,4,7,21, 2, 9, 5, 992]

#print result 
print(unOrderLinSearch(A, 4))
print(unOrderLinSearch(A, 59))


