'''
Selection Sort: 
    Sorts the smallest element from an unsorted list
'''

from re import A


def selectSmall(arr): 
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)): 
        if arr[i] < smallest: 
            smallest = arr[i]
            smallest_index = i
    return smallest_index


#print(selectSmall(arr))
'''
def selectionSort(arr): 
    newarr = []
    for i in range(1, len(arr)): 
        small = selectSmall(arr)
        newarr.append(arr.pop(small))
    return newarr
    
arr = [5,3,6,2,10]

print(selectionSort(arr))
'''
#show the highest played artists 
def highestplayed(arr):
    largest = arr[len(arr)-1]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest  = arr[i]
    return largest 


arr = [5,3,6,2,10]

print(highestplayed(arr))