class Heap:
    array = []

    def __init__(self, array=list('YRPDFBKAC')):
        self.array = array

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


def fixHeap(H, k):
    pass


def heapifying(H):
    if(H.isLeaf == False):
        heapifying(H.leftSubtree)
        heapifying(H.rightSubtree)
        k = H  # the root
        fixHeap(H, k)
