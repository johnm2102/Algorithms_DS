def insertionsort(arr): 
    for i in range(1,len(arr)):
        temp = arr[i]
        k = i 
        while k > 0 and temp < arr[k-1]:
            arr[k] = arr[k-1]
            k -= 1
        arr[k] = temp 

a = [-2, 45, 0, 11, -9]

insertionsort(a)
print(a)
        