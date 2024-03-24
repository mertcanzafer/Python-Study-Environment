graph = {
    '1': ['2', '3', '4'],
    '2': ['3'],
    '3': ['4', '5'],
    '4': ['5'],
    '5': ['6', '7'],
    '6': [],
    '7': []
}

visited = []

# We are gonna use stack data structure through calling functions


def DFS_Alg(vertex, visited, graph):
    if vertex not in visited:
        print(vertex)
        visited.append(vertex)
        for adjacent in graph[Vertex]
        # Recursive call
        DFS_Alg(adjacent,visited,graph)
