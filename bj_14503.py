n, m = map(int, input().split())
# û�� ����
clean = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())

path = []
for i in range(n):
  path.append(list(map(int, input().split())))

# ��, ��, ��, ��
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# ���� �������� Ʈ�� �Լ�
def turn_left():
  global d
  d -= 1
  if d == -1: # �� -> ��  
    d = 3  

clean[r][c] = 1
kan = 1
turn_cnt = 0

while True:  
  turn_left()
  nr = r + dr[d]
  nc = c + dc[d]
  
  if clean[nr][nc] == 0 and path[nr][nc] == 0:
    clean[nr][nc] = 1 # �̵��� ��ġ���� û��
    r, c = nr, nc
    kan += 1
    turn_cnt = 0
    continue
  else:
    turn_cnt += 1

  if turn_cnt == 4: # �� 4�� ȸ���� ���
    nr = r - dr[d] # �ٶ󺸴� ���⿡�� ����
    nc = c - dc[d] # �ٶ󺸴� ���⿡�� ����
    if path[nr][nc] == 0: # �̵��� ��ġ�� ���� �ƴ϶��
      r, c = nr, nc
    else:
      break
    turn_cnt = 0 # ȸ�� Ƚ�� �ʱ�ȭ

print(kan)