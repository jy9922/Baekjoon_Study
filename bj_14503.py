n, m = map(int, input().split())
# 청소 여부
clean = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())

path = []
for i in range(n):
  path.append(list(map(int, input().split())))

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽 방향으로 트는 함수
def turn_left():
  global d
  d -= 1
  if d == -1: # 북 -> 서  
    d = 3  

clean[r][c] = 1
kan = 1
turn_cnt = 0

while True:  
  turn_left()
  nr = r + dr[d]
  nc = c + dc[d]
  
  if clean[nr][nc] == 0 and path[nr][nc] == 0:
    clean[nr][nc] = 1 # 이동한 위치에서 청소
    r, c = nr, nc
    kan += 1
    turn_cnt = 0
    continue
  else:
    turn_cnt += 1

  if turn_cnt == 4: # 총 4번 회전한 경우
    nr = r - dr[d] # 바라보는 방향에서 후진
    nc = c - dc[d] # 바라보는 방향에서 후진
    if path[nr][nc] == 0: # 이동한 위치가 벽이 아니라면
      r, c = nr, nc
    else:
      break
    turn_cnt = 0 # 회전 횟수 초기화

print(kan)