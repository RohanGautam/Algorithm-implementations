import math
from pprint import pprint
tableSize = 11


# hash functions. Responsible for generating locations to put keys into
def modHash(x):
    '''Avoid pwr of 10 keys, prime number as table size better'''
    return x % tableSize


def multCongruential(x):
    multiplier = 8*math.floor(x) + 5
    return (x*multiplier) % tableSize


# keys that we plan to put into the table
# keys = list(range(30, 30+tableSize))
# keys = [1051, 1492, 1776, 1812, 1918, 1561, 523, 1340]
keys = [7, 23, 29, 15, 34]
# a direct address table, assuming each entry is None until assigned to by hash fn
table = [None]*tableSize


def closedAddress(index, ele):
    ''' load factor = len(keys)/tableSize = (n/h) '''
    if(type(table[index]) != list):
        table[index] = [table[index]]
    table[index].append(ele)


def openAddress(index, ele, hashFn, doubleHash=False):
    def rehashfn(x, i): return (hashFn(x)+i) % tableSize
    counter = 1
    pos = index
    while(table[pos] != None):
        if(doubleHash == True):  # Double hashing
            # positions to move ahead/back determined by another hash fn times the counter, not just plain increment. This is done to introduce more randomness.
            def anotherHashFn(x): return x % 7 + 1
            # pos = rehashfn(ele, counter*anotherHashFn(ele))
            pos = rehashfn(ele, counter*anotherHashFn(ele))
        else:  # Linear probing
            pos = rehashfn(ele, counter)
        if(table[pos] == None):
            table[pos] = ele
            break
        counter += 1  # so it tries the next location in next iteration


# putting keys into the table:


def putIntoTable(ele):
    index = modHash(ele)
    if(table[index]):
        # there's a collision! Handle it using any of the following ways:

        # closedAddress(index, ele)
        # openAddress(index, ele, modHash)
        openAddress(index, ele, modHash, doubleHash=True)
    else:
        table[index] = ele


for ele in keys:
    putIntoTable(ele)


pprint(table)
