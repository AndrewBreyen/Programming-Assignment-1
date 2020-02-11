# read in file, split into array
file = open("5.ij","r")
reader = r.reader()
listOfNums = list(reader)
nums = listOfNums[::2]


def toposort(graph):
    n = len(graph)
    v = [False] * len(graph)
    ordering = [len(graph)]
    i = n-1

    for(node in graph):
        if v[node] == false:
            visitedNodes = []
            dfs(node, v, visitedNodes, graph)
            for node in visitedNodes:
                ordering[i] = node
                i = i - 1

    return ordering

def dfs(node, v, visitedNodes, graph):
    v[node] = True

    edges = graph.getEdgesOutFromNode(node)
    for edge in edges:
        if v[edge.to] == false:
            dfs(edge.to, v, visitedNodes, graph)
        
        visitedNodes.append(node)

graph = Graph(n)
    