'''
Bubble Sort: 
    - A sorting algorithm that iterates from top to bottom of the array
    - Switch each number with each other until either list or array is sorted]
'''

# Bubble sort in Python
def bubblesort(arr):
    for i in range(len(arr)): 
        for j in range(0,len(arr) - i - 1): 
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

data = [-2, 45, 0, 11, -9]

bubblesort(data)
print(data)