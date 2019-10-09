def linearSearch(L, ele):
    for i,e in enumerate(L):
        if e==ele:
            return i+1

L = [3, 4, 2, 1, 4, 6, 7, 8, 9, 9, 11]  # data

print(linearSearch(L, 1))