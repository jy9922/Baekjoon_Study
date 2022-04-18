import sys
sys.setrecursionlimit(10**4)

t = int(sys.stdin.readline())
result = []
cnt = 0
garden = []

def input_a():
  global garden
  global cnt
  m, n, k = map(int, sys.stdin.readline().split())
  garden = [[0] * n for _ in range(m)]
  for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    garden[x][y] = 1

  for i in range(m):
    for j in range(n):
      if dfs(i, j, garden, m, n) == True:
        cnt += 1

  result.append(cnt)
  cnt = 0  

  

def dfs(x, y, garden, m, n):
  if x <= -1 or x >= m or  y <= -1 or y >= n:
    return False
  if garden[x][y] == 1:
    garden[x][y] = 0
    dfs(x-1, y, garden, m, n)
    dfs(x+1, y, garden, m, n)
    dfs(x, y-1, garden, m, n)
    dfs(x, y+1, garden, m, n)
    return True
  return False
    
      
for j in range(t):
  input_a()

for i in result:
  print(i)

