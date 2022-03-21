def dfs(x,y,count):
  global ans
  ans = max(ans,count)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      continue
    if visited[graph[nx][ny]] == 1:
      continue
    #백트래킹
    visited[graph[nx][ny]] = 1
    dfs(nx,ny,count+1)
    visited[graph[nx][ny]] = 0
    


r, c = map(int,input().split())
graph = []

for i in range(r):
  graph.append(list(map(lambda x: ord(x)-65,input()))) #아스키 코드로 반환
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [0]*26 #알파벳 26개만큼 배열 설정
visited[graph[0][0]] = 1
ans = 1
dfs(0,0,ans)
print(ans)