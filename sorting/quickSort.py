def partition(L):
    start, end, mid = 0, len(L), len(L)//2
    L[start], L[mid] = L[mid], L[start]  # move pivot to the beginning
    pivot = L[start]  # make pivot the middle value (it was swapped with the first). We need it's value so we can make comparisions with it later on
    last_small = start  # last_small keeps track of he boundary between the portions of the list smaller and bigger than the pivot

    for i in range(last_small+1, end): # in L[1:]
        if L[i] < pivot:
            ''' If current is smaller than pivot, swap it with 
            ele after the last_small, and update last_small
            to be the index of that element. To visualize easier,
            think of a case [P, a, b, _c, _d, e, f, g] where you are 
            at the index of e with last_small at index of b.
            a,b,e,f,g are smaller than P and _c, _d are bigger than P'''
            L[i], L[last_small+1] = L[last_small+1], L[i]
            last_small += 1

    L[last_small], L[start] = L[start], L[last_small]
    return (last_small, L)


def quickSort(L):
    if len(L) <= 1:
        return L
    else : 
        pivotPos, L = partition(L)
        L[:pivotPos] = quickSort(L[:pivotPos])
        L[pivotPos+1:] = quickSort(L[pivotPos+1:]) # pivotPos is already sorted so only sort before and after it
        return L





L = [4, 3, 5, 6, 7, 19, 0, 9, 12]
# print(L)
print(partition(L))
# print(quickSort(L))
