'''
Inversion Counter: 
    Counts the number of inversions in an array
    Uses mergesort 
'''

def inversioncount(ar, x): 
    counter = 0
    for i in range(x): 
        for j in range(i + 1, x):
            if (ar[i] > ar[j]): 
                counter  += 1 
    return counter
        


ar = [6,2,1,6,4,8,10]
x = len(ar)

print(inversioncount(ar,x))