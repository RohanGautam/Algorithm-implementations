def merge(L1, L2):
    '''
    Suppose L1 and L2 are as shown below, initially:    
    [1,2,3,4], [1,3,4,5]      => []
    ^           ^                ^
    a           b               mergedList

    a,b will refer to elements at position a,b.
    The merge function merges in the following manner:
    * if a=b, then both added to merged list
    * if a<b, then a added to list, it's counter incremented
    * if b<a, then b added to list, it's counter incremented
    * if b's list is exhausted, then remaining of a is directly added to mergedList
    * if a's list is exhausted, then remaining of b is directly added to mergedList

    '''
    a, b = 0, 0
    mergedList = []
    while(a < len(L1) and b < len(L2)):
        if(L1[a] < L2[b]):
            mergedList.append(L1[a])
            a += 1
        elif(L2[b] < L1[a]):
            mergedList.append(L2[b])
            b += 1
        elif(L1[a] == L2[b]):
            mergedList.append(L1[a])
            mergedList.append(L1[b])
            a += 1
            b += 1
    else:  # executed only when condition is false. don't need 'else', but for easier readability
        if(a < len(L1)):  # means b was >=len(L2)
            mergedList.extend(L1[a:])
        if(b < len(L2)):  # means a was >=len(L2)
            mergedList.extend(L2[b:])

    return mergedList


def mergeSort(L):
    start, end = 0, len(L)-1
    mid = (start+end)//2 + 1 # +1, otherwise in [a,b], mid will be 0.
    if((end-start) <= 0): # same as end<=start
        return L
    else: # if end>start
        # merge the two sorted halves
        return merge(mergeSort(L[:mid]), mergeSort(L[mid:]))


mergeSort([4, 3, 5, 6, 7, 1, 0, 9, 12])
