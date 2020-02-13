import time as t
import sys

# an array to hold boolean values if a vertex was previously visited
visited = []

# initiates the topoSort.
# visitedVertex: the result of dfs(visitedVertex, g, v, stack) -- recursive
# g: graph holding nodes and their connections
# v: a specific vertex
def topoSort(visitedVertex, g, v):
    stack = []
    visitedVertex = dfs(visitedVertex, g, v, stack)
    for vertex in g.keys():
        if vertex not in visitedVertex:
            dfs(visitedVertex, g, vertex, stack)
    return stack

# recursive method to do the depth first sort
# visited: an array containing if nodes were visited
# g: graph holding nodes and their connections
# stack: the stack (defined in the topoSort method)
def dfs(visited, g, v, stack):
    visited.append(v)
    if v in g:
        for w in g[v]:
            if w not in visited:
                dfs(visited, g, w, stack)
    stack.append(v)
    return visited

# startProgram "MainMethod"

# sys.argv[1] takes the 1st parameter from command line (0th param is just the path to the program itself) 
theFile = open(sys.argv[1], "r")
lines = theFile.readlines()

# 2D array for storing vertexes and their targets
vertex, targetVertex = [], []

#put vertexes and their targets into the 2D array. This will be used later
for line in lines:
    vertex.append(line.split()[0])
    targetVertex.append(line.split()[1])

# an empty dictionary for holding the nodes and their connections
graph = {}

# put vertexes into the graph.
# The "|=" part on the first action in the if statement takes into consideration all nodes connected to first node. 
# Without it, it just considers the last connected node.
for i in range(len(lines)):
    v = vertex[i]
    if v in graph:
        graph[v] |= set([targetVertex[i]])
    else:
        graph[v] = set([targetVertex[i]])

# start timer for execution time
start = t.time()

# here's actually where the sort is done
print("doTheSort!")
topoOrder = topoSort(visited, graph, vertex[0])


# pop elements off the stack. This will be the result of the sort!
for i in range(len(visited)):
    print(topoOrder.pop())

# end timer for execution time
end = t.time()

# calculate total execution time
totalTime = end - start

# print execution time
print("Execution Time in Seconds: "+str(totalTime))
