graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def bfs(graph, node): #function for BFS
    visited = []
    visited.append(node)

    q = []
    q.append(node)

    while q:          # Creating loop to visit each node
        cur = q.pop(0)
        print(cur, end=" ")

        for neighbour in graph[cur]:
          if neighbour not in visited:
            visited.append(neighbour)
            q.append(neighbour)

bfs(graph, '5')