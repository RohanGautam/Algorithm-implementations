import os
import sys
# to be able to run it even if I'm not in the directory currently
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from stack import Stack
from anytree import Node, RenderTree
'''
Implementation of DFS - depth first search
> Go as deep as you can, then backtrack back, and go deep again.
> If v->neighbours[w1,w2,w3..], visit all vertices adjacent to w1, then backtrack, then continue with [w2...]
> Can be used to find solutions to something by exhausting possibilities, because of it's nature of going in depth

picture of graph being used: ../graphImage/graph1.png

# Time complexity, worst case: [same as bfs]
Θ(V+E) if adjacency list
Θ(V^2) if adjacency matrix (here)
'''
nodeNames = 'ABCDEFG'
indexmap = dict(zip(range(len(nodeNames)), nodeNames))
# mark all unvisited at first
visited = dict(zip(nodeNames, [False]*len(nodeNames)))

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

# recursive dfs (stack implicitly used)
def dfs_recursive(graph, nodeName, treeNode):
    visited[nodeName] = True
    row = graph[indexOfNode(nodeName)]
    neighbours = [indexmap[i] for i in range(len(row)) if row[i] == 1]
    for neighbour in neighbours:
        if visited[neighbour] == False:
            # will be marked visited in it's recursive call itself. Also thr current node is the parent for it's neighbour, as can be seen from what's being passed to the function.
            dfs_recursive(graph, neighbour, Node(neighbour, parent=treeNode))
    return treeNode


def dfs_stack(graph, startNode):
    ''' TODO: this is faulty:/ fix it! '''
    visited[startNode] = True
    s = Stack()
    s.push(startNode)
    currentNodeName = s.pop()
    while True:
        row = graph[indexOfNode(currentNodeName)]
        neighbours = [indexmap[i] for i in range(len(row)) if row[i] == 1]
        for neighbour in neighbours:
            if(visited[neighbour] == False):
                print(f'currently visiting {neighbour} parent is {currentNodeName}')
                visited[neighbour]= True
                currentNodeName = neighbour
                s.push(neighbour)
                break
        # if no more neighbours to visit, backtrack
        print('')
        if(any([visited[neighbour]==False for neighbour in neighbours])==False):
            if s.isEmpty() : break
            currentNodeName = s.pop()
        


startNodeName = 'A'

# dfs_stack(adjList, startNodeName)

dfs_tree = dfs_recursive(adjList, startNodeName, Node(startNodeName))

# `anytree` keeps track of the connections we make to the parent node.
#  So in the end, we just render it (it also supports great visualisation!)
for pre, fill, node in RenderTree(dfs_tree):
    print(f'{pre}{node.name}')

# G, E unreachable from 'A', thats why not seen in the dfs tree