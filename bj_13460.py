from collections import deque

n, m = map(int,input().split())
map = []
for i in range(m):
  map.append(list(input()))

# 왼, 오, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0

def bfs(map,x,y):
  global result
  queue = deque()
  queue.append((x, y))

  while queue:
    print('큐 :', queue)
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx > n or ny < 0 or ny > m:
        continue
      if map[nx][ny] == '#':
        continue
      if map[nx][ny] == 'O':
        result += 1
        break
      elif map[nx][ny] == '.':
        while True:
          nx += dx[i]
          ny += dy[i]
          if map[nx][ny] == '#':
            nx -= dx[i]
            ny -= dy[i]
            print("nx, ny : ", nx, ny)
            break
          else:
            map[nx][ny] = '#'
        result += 1
        if map[nx][ny] == 'O':
          break
        queue.append((nx,ny))
        
  return result
           

for i in range(n):
      for j in range(m):
        if map[i][j] == 'R':
          x, y = i, j
print(x,y)
print(bfs(map,x, y))
    
    
  
  