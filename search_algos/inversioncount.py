'''
Inversion Counter: 
    Counts the number of inversions in an array
'''

def inversioncount(array, x): 
    counter = 0
    for i in range(x):
        for j in range(i + 1, x):
            if (array[i] > array[j]):
                counter += 1
    return counter 
        


array_1 = [6,2,1,6,4,8,10]
x = len(array_1)

print(inversioncount(array_1,x))