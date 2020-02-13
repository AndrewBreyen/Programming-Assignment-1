#tsort.py
import time as T
import sys

#print(graph)
visited = []

#"""
def dfs(visited, G, V, stack):
    visited.append(V)
    if V in G:
        for w in G[V]:
            if w not in visited:
                dfs(visited, G, w, stack)
    stack.append(V)
    return visited

def topologicalSorting(visitedV, G, V):
    stack = []
    visitedV = dfs(visitedV, G, V, stack)
    for vertex in G.keys():
        if vertex not in visitedV:
            dfs(visitedV, G, vertex, stack)
            #visited.append(vertex)
    return stack
    #return visitedV

###########   PROGRAM STARTS HERE   ##############################################

f = open(sys.argv[1], "r")
lines = f.readlines()

#following code inspired by the one found here: 
#https://stackoverflow.com/questions/47242038/creating-a-graph-using-input-from-text-file-in-python
vertex, target_vertex = [], []
for line in lines:
    vertex.append(line.split()[0])
    target_vertex.append(line.split()[1])

graph = {}
for i in range(len(lines)):
    v = vertex[i]
    if v in graph:
        graph[v] |= set([target_vertex[i]])
    else:
        graph[v] = set([target_vertex[i]])

startTime = T.time()
topological_order = topologicalSorting(visited, graph, vertex[0])
for i in range(len(visited)):
    print(topological_order.pop())

print("%.10f seconds" %(T.time() - startTime))
###
