from anytree import Node, RenderTree

nodeNames = 'ABCD'
indexmap = dict(zip(range(len(nodeNames)), nodeNames))

# undirected, fully connected graph, so symmetric about main diagonal
adjList = [
    [0, 20, 35, 15],
    [20, 0, 25, 10],
    [35, 25, 0, 12],
    [15, 10, 12, 0],
]

def viewConnections():
    for i, row in enumerate(adjList):
        connections = [indexmap[i] for i in range(len(row)) if row[i] == 1]
        print(f'{indexmap[i]} connected to {connections}')

def indexOfNode(letter):
    return nodeNames.index(letter)

flatten = lambda l: [item for sublist in l for item in sublist]
weight = lambda x,y: adjList[indexOfNode(x)][indexOfNode(y)]

def minWtVertex(node, cycle):
    row = adjList[indexOfNode(node)]
    neighbours = [indexmap[i] for i in range(len(row)) if row[i]!=0] 
    unvisitedNeighboursFromNode = [(node,x, weight(node,x)) for x in neighbours if x not in flatten(cycle)]
    if unvisitedNeighboursFromNode != []:
        return sorted(unvisitedNeighboursFromNode, key = lambda x: x[2])[0]
    return -1

def hasVertexNotInCycle(cycle):
    for x in nodeNames:
        if x not in set(flatten(cycle)):
            return True
    return False

def nearestNeighbour(start):
    cycle = []
    cost = 0
    current = start
    while (hasVertexNotInCycle(cycle)):
        current, nextVertex, wt = minWtVertex(current, cycle)
        cost+=wt
        cycle.append((current,nextVertex))
        current=nextVertex
    
    # as can see from this, this assumes the last one `will` be connected to the start node
    cycle.append((current, start))
    cost += weight(current, start)
    print(f'total cost is {cost}')
    return cycle

print('path to follow via nearest neighbour algorithm')
print(nearestNeighbour('A'))

