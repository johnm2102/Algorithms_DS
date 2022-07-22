def mergesort(arr):
    if len(arr) > 1: 
        mid = len(arr)//2 
        lo = arr[:mid]
        hi = arr[mid:]
        mergesort(lo)
        mergesort(hi)

incomplte 



arr = [3,4,0,8,3,4,0]
mergesort(arr)
print(arr)