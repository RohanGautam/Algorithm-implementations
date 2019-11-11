import queue
from anytree import Node, RenderTree
'''
# Implementation of BFS - Breadth first search
>Visit all neighbours of current node, before visiting the other neighbours of neighbours.
>Can be used to find shortest path
picture of graph being used: ../graphImage/graph1.png
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

# bfs tree not implemented. without the tree, it's just traversal
def bfs(graph, startNode, visitNext):
    # mark startnode as visited
    visited[startNode] = True
    visitNext.put(startNode)
    print(f'putting startnode : {startNode}')
    # >> add startNode to tree <<
    firstNode = Node(startNode)
    secondLastLevelNode = firstNode
    count=0
    while visitNext.empty() == False:
        currentNode = visitNext.get()
        if count == 0 :  # if first ele, current node is firstNode
            currentTreeNode = firstNode
            count+=1
        else :
            for childOfSecondLastLevel in secondLastLevelNode.children:
                # if the node appears in a level before, make that the current node instead of initialising a new one
                if childOfSecondLastLevel.name == currentNode:
                    currentTreeNode = childOfSecondLastLevel
        secondLastLevelNode = currentTreeNode

        row = graph[indexOfNode(currentNode)]
        neighbours = [indexmap[i] for i in range(len(row)) if row[i] == 1]
        for node in neighbours:
            if(visited[node] == False):
                visited[node] = True
                visitNext.put(node)
                # >> add edge between node and currentNode to tree <<
                Node(node, parent=currentTreeNode)
                print(f'visited, putting: {node}, parent is {currentNode}')
    return RenderTree(firstNode)

# G,E are unreachable
bfsTree = bfs(adjList, 'A', visitNext) # passing these so it's clear what it needs if global variables not present
print('bfs tree :')
for pre, fill, node in bfsTree:
    print("%s%s" % (pre, node.name))