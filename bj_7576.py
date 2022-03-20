from collections import deque

def bfs(m,n,v,count):
  queue = deque()
  for i in range(m):
    for j in range(n):
      if graph[i][j] == 1:
        x, y = i, j
        queue.append((x,y))
        graph[x][y] = 1
        count.append(graph[x][y])
  while queue:
    x, y = queue.popleft()
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1 or graph[nx][ny] == -1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        v = graph[nx][ny]
        count.append(v)
        queue.append((nx,ny))
  for i in range(m):
    for j in range(n):
      if graph[i][j] == 0:
        return -1
  
n, m = map(int, input().split())

graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
v = 0
count = []


bfs(m,n,v,count)
if bfs(m,n,v,count) == -1:
  print(-1)
else:
  print(max(count)-1)
