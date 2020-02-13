import time as t
import sys

visited = []

def dfs(visited, g, v, stack):
    visited.append(v)
    if v in g:
        for w in g[v]:
            if w not in visited:
                dfs(visited, g, w, stack)
    stack.append(v)
    return visited

def topoSort(visitedVertex, g, v):
    stack = []
    visitedVertex = dfs(visitedVertex, g, v, stack)
    for vertex in g.keys():
        if vertex not in visitedVertex:
            dfs(visitedVertex, g, vertex, stack)
    return stack

#startProgramMainMethod
theFile = open(sys.argv[1], "r")
lines = theFile.readlines()

vertex, targetVertex = [], []

for line in lines:
    vertex.append(line.split()[0])
    targetVertex.append(line.split()[0])


graph = {}

for i in range(len(lines)):
    v = vertex[i]
    if v in graph:
        graph[v] |= set([targetVertex[i]])
    else:
        graph[v] = set([targetVertex[i]])

start = t.time()

topoOrder = topoSort(visited, graph, vertex[0])

print("doTheSort!")

for i in range(len(visited)):
    print(topoOrder.pop())

end = t.time()

totalTime = end - start
print("Execution Time in Seconds: "+str(totalTime))
