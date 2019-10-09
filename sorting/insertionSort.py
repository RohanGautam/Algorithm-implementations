def insertionSort(L):
    ''' Consider the element in the unsorted part(L[i]) along with all the 
    elements in the sorted part(L[:i]), and sort them all(L[:i]+L[i]) together'''
    for i in range(1, len(L)):
        # from i->1 backwards, L[0] not included because we doing j-1 to compare
        for j in range(i, 0, -1):
            if L[j] < L[j-1]: 
                L[j-1], L[j] = L[j], L[j-1]
            else:
                break
    return L


def insertionSortMyVersion(L):
    ''' take the element in unsorted part (L[i]),
     compare it with every element in the sorted part (L[j])'''
    for i in range(1, len(L)):
        for j in range(0, i):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
            else:
                break
    return L


L = [2, 5, 4, 7, 8, 9, 1, 6, 0, 14]
print(insertionSort(L))
print(insertionSortMyVersion(L))
