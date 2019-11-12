from anytree import Node, RenderTree

nodeNames = 'SUVXY'
indexmap = dict(zip(range(len(nodeNames)), nodeNames))
# mark all unvisited at first
large_number = 100000
d = dict(zip(nodeNames, [large_number]*len(nodeNames)))
pi = dict(zip(nodeNames, [None]*len(nodeNames)))
S = dict(zip(nodeNames, [0]*len(nodeNames)))


adjList = [
    [0, 10, 0, 5, 0],
    [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 3, 9, 0, 2],
    [7, 0, 6, 0, 0]
]

def indexOfNode(letter):
    return nodeNames.index(letter)

def extractCheapest(sortedVertices):
    # because it's sorted. This fn exists to make it a bit clearer
    return sortedVertices[0]

def weight(node1, node2) : 
    return adjList[indexOfNode(node1)][indexOfNode(node2)]

def dijkstras(graph, source):
    d[source] = 0
    # should ideally use priority queue, but the idea is to maintain an order of vertices according to their distance, which is what is being done here
    sortedVertices = sorted(list(nodeNames), key= lambda x : d[x])
    while len(sortedVertices) != 0 :
        current = extractCheapest(sortedVertices)
        sortedVertices = sortedVertices[1:]
        S[current] = 1 # current is the cheapest, based on D, thus add it to S, signifying it's min dist with src has been found
        row = graph[indexOfNode(current)]
        neighbours = [indexmap[i] for i in range(len(row)) if row[i] != 0]
        for neighbour in neighbours:
            ''' S[neighbour]!=1 means if it's in the set V-S, the condn says that if the new calculated distance is smaller than the current dist'''
            if (S[neighbour]!=1 and (d[neighbour]> d[current] + weight(current, neighbour))):
                sortedVertices.remove(neighbour)
                d[neighbour] = d[current] + weight(current, neighbour) # update to a smaller weight
                pi[neighbour] = current
                sortedVertices = sorted(sortedVertices+[neighbour], key= lambda x : d[x])
    return(S, d, pi)
    
source = 'S'
S, d, pi = dijkstras(adjList, source)
pi[source]=0
print(f'{S}\n{d}\n{pi}')

