import queue
'''
Implementation of BFS - Breadth first search
using: ../graphImage/graph1.png
'''
nodeNames = 'ABCDEFG'
indexmap = dict(zip(range(len(nodeNames)), nodeNames))
# mark all unvisited at first
visited = dict(zip(nodeNames, [False]*len(nodeNames)))
visitNext = queue.Queue()

adjList = [
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0]
]


def viewConnections():
    for i, row in enumerate(adjList):
        connections = [indexmap[i] for i in range(len(row)) if row[i] == 1]
        print(f'{indexmap[i]} connected to {connections}')

# viewConnections()


def indexOfNode(letter):
    return ord(letter)-65  # for uppercase letters only

# bfs tree not implemented
def bfs(graph, startNode, visitNext):
    # mark startnode as visited
    visited[startNode] = True
    visitNext.put(startNode)
    print(f'putting startnode : {startNode}')
    # >> add startNode to tree <<
    while visitNext.empty() == False:
        currentNode = visitNext.get()
        row = graph[indexOfNode(currentNode)]
        neighbours = [indexmap[i] for i in range(len(row)) if row[i] == 1]
        for node in neighbours:
            if(visited[node] == False):
                visited[node] = True
                visitNext.put(node)
                print(f'visited, putting: {node}')
                # >> add edge between node and currentNode to tree <<

# G,E are unreachable
bfs(adjList, 'A', visitNext) # passing these so it's clear what it needs if global variables not present