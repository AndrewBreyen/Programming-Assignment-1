visited = []
stack = []

def dfs(visited, G, V):
    visited.append(V)
    if V in G:
        for w in G[V]:
            if w not in visited:
                dfs(visited, G, w)
    return visited

    file = open("wiki.ij", "r")
    lines = f.readLines()

    vertex, targetVertex = [], []
    for line in lines:
        vertex.append(line.split()[0])
        targetVertex.append(line.split()[1])
        
    graph = {}
    
    for i in range(len(lines)):
        v = vertex[i]
        if v in graph:
            graph[v] |= set([targetVertex[i]])
        else:
            graph[v] = set([targetVertex[i]])

topologicalOrder = dfs(visited, graph, vertex[0])
topologicalOrder.reverse()
print(topologicalOrder)