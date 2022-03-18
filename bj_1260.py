from collections import deque

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(new_graph,i,visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
 
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        
n, m, v = map(int, input().split())
graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))

new_graph = [[] for _ in range(n+1)]

  
for j in range(1,n+1):
  for i in range(m):
    if graph[i][0] == j:
      new_graph[j].append(graph[i][1])
      
    if graph[i][1] == j:
      new_graph[j].append(graph[i][0])

for j in range(1,n+1):
  new_graph[j].sort()


visited = [False] * (n+1)
dfs(new_graph,v,visited)
print()
visited = [False] * (n+1)
bfs(new_graph,v,visited)
