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
def dfs_recursive(graph, node):
    visited[node] = True
    row = graph[indexOfNode(node)]
    neighbours = [indexmap[i] for i in range(len(row)) if row[i] == 1]
    for neighbour in neighbours:
        if visited[neighbour] == False:
            print(f'visited {neighbour}, parent is {node}')
            dfs_recursive(graph, neighbour) # will be marked visited in it's recursive call itself.

dfs_recursive(adjList, 'A')