graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(set(), graph, '5')