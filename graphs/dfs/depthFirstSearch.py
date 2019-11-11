from anytree import Node, RenderTree
'''
Implementation of DFS - depth first search
> Go as deep as you can, then backtrack back, and go deep again.
> If v->neighbours[w1,w2,w3..], visit all vertices adjacent to w1, then backtrack, then continue with [w2...]
> Can be used to find solutions to something by exhausting possibilities, because of it's nature of going in depth
picture of graph being used: ../graphImage/graph1.png
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

startNodeName = 'A'
dfs_tree = dfs_recursive(adjList, startNodeName, Node(startNodeName))

# `anytree` keeps track of the connections we make to the parent node.
#  So in the end, we just render it (it also supports great visualisation!)
for pre, fill, node in RenderTree(dfs_tree):
    print(f'{pre}{node.name}')

# G, E unreachable