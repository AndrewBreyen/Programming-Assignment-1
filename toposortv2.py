import time as time
import sys

visited = []

def dfs(visited, g, v, stack):
    visited.append(v)
    if v in g:
        for w in g[v]
            if w not in visited:
                dfs(visited, g, w, stack)
    stack.append(v)
    return visited

def topoSort(visitedVertex, g, v):
    stack = []
    visitedVertex = dfs(visitedVertex, g, v, stack)
    for vertex in g.keys():
        if vertex not in visited v:
            dfs(visitedVertex, g, vertex, stack)
    return stack

#startProgramMainMethod
theFile = open(sys.argv[1], "r")
lines = f.readLines()

vertex, targetVertex = []. []

for line in lines:
    vertex.append(line.split()[0])
    targetVertex.append(line.split()[1])

theGraph = {}

for i in range(len(lines)):
    v = vertex[i]
    if v in graph:
        graph[v] |= set([targetVertex[i]])
    else:
        graph[v] = set([target])

start = time.time

topoOrder = topoSort(visited, graph, vertex[0])

for i in range(len(visited)):
    print(topoOrder.pop)