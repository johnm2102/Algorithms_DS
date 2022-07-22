'''
Selection Sort: 
    Sorts the smallest element from an unsorted list
'''

def selectionSort(arr):
    for i in range(len(arr)):
        least = i
        for k in range(i + 1, len(arr)):
            if arr[k]<arr[least]:
                min_num = k
        swap(arr, least, i)

def swap(arr, x, y):
    temp = arr[x] 
    arr[x] = arr[y]
    arr[y] = temp 

    
arra = [5,3,6,2,10]

print(selectionSort(arra))