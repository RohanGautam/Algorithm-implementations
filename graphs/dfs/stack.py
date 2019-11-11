class Stack:
    '''a really basic stack implementation'''
    L=[]
    def __init__(self):
        self.L = []
    def push(self, ele):
        self.L.append(ele)
    def pop(self):
        return self.L.pop()
    def isEmpty(self):
        return len(self.L) == 0