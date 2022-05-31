"""
iterpolation search: 
    a variant of binary search
"""
def intSearch(numList, val):
    lo = 0 
    hi = len(numList)-1
    while numList[lo] <= val and numList[hi] >= val:
        mid = (lo + ((val - numList[lo])*(hi - lo))/(numList[hi] - numList[lo])
        if numList[mid] < val:
            lo = mid + 1
        elif numList[mid] > val:
            hi = mid - 1
        else:
            return mid 
    
    if numList[lo] == val:
        return lo 
    
    return None 
