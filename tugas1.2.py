graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G'],
}


visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
    
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
print("Hasil penelusuran graf menggunakan dfs:")
dfs(visited, graph, 'D')