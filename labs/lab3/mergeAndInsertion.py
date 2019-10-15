import random, time, csv, copy


class mergeAndInsertion():
    
    dataset = []
    datasize = 0
    keyCmpCounter = 0
    timeTaken=0
    def __init__(self, dataset):
        self.dataset = dataset
        self.datasize = len(dataset)
        self.keyCmpCounter = 0
        self.timeTaken = 0

    def generateData(self):
        self.dataset = [random.randint(1, self.datasize) for _ in range(self.datasize)]

    def merge(self, first, last):
        ''' consider two arrays to be merged as one, the start pointers are first and ((first+last)/2) '''
        dataset = self.dataset
        a, mid = first, (first+last)//2
        b = mid+1

        if last-first <= 0:
            return

        while (a <= mid and b <= last):
            if dataset[a] > dataset[b]:
                self.keyCmpCounter+=1
                temp = dataset[b] 
                b += 1
                mid += 1
                for i in range(mid, a, -1):
                    dataset[i] = dataset[i-1]
                dataset[a] = temp
                a += 1
            elif dataset[a] < dataset[b]:
                self.keyCmpCounter+=2
                a += 1
            else:
                self.keyCmpCounter+=2
                if(a == mid and b == last):
                    break
                temp = dataset[b]
                b += 1
                a += 1
                mid += 1
                for i in range(mid, a, -1):
                    dataset[i] = dataset[i-1]
                dataset[a] = temp
                a += 1

    def mergeSort(self, first, last):
        mid = (first+last)//2
        if(last-first <= 0):
            return
        else:
            self.mergeSort(first, mid)
            self.mergeSort(mid+1, last)
            self.merge(first, last)
    
    def insertionSort(self,first,last):
        dataset = self.dataset
        for i in range(first+1, last - first + 1):
            # from i->1 backwards, L[0] not included because we doing j-1 to compare
            for j in range(i, 0, -1):
                if dataset[j] < dataset[j-1]: 
                    self.keyCmpCounter+=1
                    dataset[j-1], dataset[j] = dataset[j], dataset[j-1]
                else:
                    self.keyCmpCounter+=1
                    break
    
    def mergeSortModified(self, first, last, S):
        mid = (first+last)//2
        if(last-first > S): 
            self.mergeSortModified(first, mid, S)
            self.mergeSortModified(mid+1, last, S)
            self.merge(first, last)
        else:
            self.insertionSort(first,last)
    
    def testMergeModified(self, S):
        # self.generateData()
        # print(f'Data generated: \n{self.dataset}')
        s = time.perf_counter_ns()
        self.mergeSortModified(0, self.datasize-1, S)
        e = time.perf_counter_ns()
        self.timeTaken = e-s
        # print(f'After merging for S = {S}:\t\n time elapsed {self.timeTaken} \t\n key comparisons {self.keyCmpCounter}')
        # print('data sorted: ', self.dataset)
        # self.keyCmpCounter = 0
    
    def testMerge(self):
        # self.generateData()
        # print(f'Data generated: \n{self.dataset}')
        s = time.perf_counter_ns()
        self.mergeSort(0, self.datasize-1)
        e = time.perf_counter_ns()
        self.timeTaken = e-s
        # print(f'After merging: \n{self.dataset}')

    def testInsertion(self):
        self.generateData()
        print(f'Data generated: \n{self.dataset}')
        self.insertionSort(0, self.datasize-1)
        print(f'After Insertion: \n{self.dataset}')



# m.generateData()

# size =100
# with open('analysisFolder/analysis.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['S', 'keycmp', 'timeTaken'])
#     data = [random.randint(1, 20000) for _ in range(size)]
#     for i in range(0,size) : 
#         m = mergeAndInsertion(data)
#         m.testMergeModified(i)
#         writer.writerow([i, m.keyCmpCounter, m.timeTaken])


n=1000
data = [random.randint(1, 20000) for _ in range(n)] # below fine if you run it the second time?!
# testing mergesort
m=mergeAndInsertion(copy.deepcopy(data))
# print('time taken:',m.timeTaken)
m.testMerge()
mergeTime = m.timeTaken
mergeComparisons = m.keyCmpCounter
print('Mergesort:')
print(f'\ttime taken : {mergeTime}ns \n\tkeyComparisons : {mergeComparisons}')

m2=mergeAndInsertion(copy.deepcopy(data))
# print('time taken:',m.timeTaken)
m2.testMerge()
mergeTime = m2.timeTaken
mergeComparisons = m2.keyCmpCounter
print('Mergesort:')
print(f'\ttime taken : {mergeTime}ns \n\tkeyComparisons : {mergeComparisons}')