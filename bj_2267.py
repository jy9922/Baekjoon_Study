def dfs(x,y,check):
  
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False

  if graph[x][y] == 0:
    return False
    
  if graph[x][y] == 1:
    graph[x][y] = 0
    check.append(1)
    dfs(x-1,y,check)
    dfs(x+1,y,check)
    dfs(x,y-1,check)
    dfs(x,y+1,check)
    return True
  return False
  
n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

check = []
result = 0
count = []
for i in range(n):
  for j in range(n):
    check = []
    if dfs(i,j,check) == True:
      result += 1
      count.append(len(check))

print(result)
count.sort()
for i in range(len(count)):
  print(count[i])

