graph = {
    'A' : ['B','E'],
    'B' : ['A','F'],
    'C' : ['D','G'],
    'D' : ['C','H'],
    'E' : ['A','F'],
    'F' : ['B','E'],
    'G' : ['C','H'],
    'H' : ['D','G'],
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end="")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("Hasil penelusuran graf menggunakan bfs:")
bfs(visited, graph, '')