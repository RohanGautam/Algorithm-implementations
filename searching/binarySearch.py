
# recursive implementation
def binarySearch(L, start, end, ele):
    if start > end:
        return -1
    else:
        mid =(start+end)//2
        if ele > L[mid]:
            return binarySearch(L, mid+1, end, ele)
        elif ele < L[mid]:
            return binarySearch(L, start, mid-1, ele)
        else:
            return mid

# iterative implementation
def binarySearch2(L, ele):
    start, end = 0, len(L)-1
    while(start <= end):
        mid = (start+end)//2
        if ele > L[mid]:
            start = mid+1
        elif ele < L[mid]:
            end = mid-1
        else:
            return mid
    return -1


L = [3, 4, 2, 1, 4, 6, 7, 8, 9, 9, 11]  # data
L = sorted(L)  # sort the data first
print(L)

ele = 7
print(binarySearch(L, 0, len(L)-1, ele))
print(binarySearch2(L, ele))
