from anytree import Node, RenderTree
class Heap:
    array = []

    def __init__(self, array=list('YRPDFBKAC')):
        self.array = array
    
    def printHeap(self):
        nodes = [Node(x) for x in self.array]
        for i, x in enumerate(self.array[1:]):
            nodes[i+1] = Node(x, parent= nodes[(i)//2])
        for pre, fill, node in RenderTree(nodes[0]):
            print(f'{pre}{node.name}')

    def eleAtPos(self, pos):
        if pos in range(len(self.array)):
            return self.array[pos-1]
        else:
            return -1

    def posOfEle(self, ele):
        return self.array.index(ele)+1

    def parentOfEle(self, ele):
        # these are if pos from 1 onwards
        return self.eleAtPos(self.posOfEle(ele)//2)

    def leftSubtree(self, ele):
        return self.eleAtPos(2*self.posOfEle(ele))

    def rightSubtree(self, ele):
        return self.eleAtPos(2*self.posOfEle(ele)+1)

    def isLeaf(self, ele):
        return self.eleAtPos(2*self.posOfEle(ele)) == -1

    def popRightmost(self):
        last = self.array[-1]
        self.array = self.array[:-1]
        return last

    def fixHeap(self, k, fromDeleteMax = False): # H, k but here H is global
        '''
        fixes subheap at given root k.
        example:
        ```
        h= Heap(list('CRPDFBKA'))
        h.printHeap()
        h.fixHeap('C')
        h.printHeap()
        ```
        '''
        if fromDeleteMax:
            '''if from deletemax, we are replacing the root with k[the smallest][happens at the end of fn]
            After this, we continue to fix the heap
            '''
            root = 0
            left = 1
        else:
            '''we want to fix subheap where k is the root'''
            root = self.array.index(k) # k is the root of where the subheap begins
            left = 2*self.array.index(k)+1
            
        # finding position to put k in
        while left < len(self.array):
            if left+1 < len(self.array) and self.array[left] < self.array[left+1]:
                left+=1
            if k>self.array[left]:
                break
            self.array[root], self.array[left] = self.array[left], self.array[root]
            root = left
            left = 2*root + 1 # +1 here becasue index starting
        # putting k in found location
        self.array[root] = k
    
    def constructHeap(self):
        # put elements into heap structure in arbitrary order (done during initialisation)
        self.heapify(0)

    def heapify(self, heapIndex):
        isLeaf = True if 2*(heapIndex+1)>len(self.array) else False
        if not isLeaf:
            self.heapify(2*heapIndex+1) # the left subtree
            self.heapify(2*heapIndex+2) # the right subtree
            self.fixHeap(self.array[heapIndex])
    
    def getMax(self):
        return self.array[0]
    def deleteMax(self):
        smallest = self.array[-1] # copy last(smallest) element
        self.array = self.array[:-1] # delete last element
        self.fixHeap(smallest, fromDeleteMax=True)

    def heapsort(self):
        self.constructHeap()
        for i in range(len(self.array)-1, -1, -1):
            curMax = self.getMax()
            self.deleteMax() # deletes max and fixes the heap
            self.array.append(curMax)
        print(self.array)
        self.printHeap()




        



h= Heap(list('ABCDFKPRY'))
h.heapsort()
# h.printHeap()
# h.constructHeap()
# # h.fixHeap('B')
# h.printHeap()

# # example that heaps are not unique, the output below is also a heap
# h2 = Heap()
# h2.printHeap()

