n, m = map(int, input().split())

d =[[0] * m for _ in range(n)] # û�� ���θ� list�� ���� 
x, y, direction = map(int, input().split()) # x, y, direction�� �Է� ���� 
d[x][y] = 1 # ���� ��ġ û�� (0->1) 

array = [] # �� ĭ, ���� �Է� ���� 
for i in range(n): # n ���� rows�� ���ؼ� �� row�� �Է��� ����
  array.append(list(map(int, input().split()))) #�Է��� list ���·� array�� append 
  
  dx = [-1,0,1,0] 
  dy = [0,1,0,-1] 
  
  # 0: ���� �̵�, 1: ������ �̵�, 2: �Ʒ� �̵�, 3: ���� �̵� 
  
def turn_left(): # �������� Ʈ�� �Լ� 
  global direction # global �Լ� ���� 
  direction -= 1 # �������� �̵� 
  # 0 : ��, 1 : ��, 2 : ��, 3 : �� 
  if direction == -1: # ������ �Ǵ� ���, 
    direction = 3 # 3���� �ʱ�ȭ 
    
count = 1 # ���� ��ġ�� û�� �������� 1 
turn_time = 0 # ���� �������� ȸ���ϴ� Ƚ�� ���, 4���� ��� �ٸ� ���� ���� 
while True: 
  turn_left() # ���� �������� ȸ�� 
  nx = x + dx[direction] # ���� �������� �̵� 
  ny = y + dy[direction] # ���� �������� �̵� 
      
  if d[nx][ny] == 0 and array[nx][ny] == 0: # �̵��� �ߴµ�, �湮���� �ʾҰų�, �� ������ ��� 
    d[nx][ny] = 1 # �̵��� ��ġ���� û��, 0->1 
    x = nx # ��ġ �̵� 
    y = ny # ��ġ �̵� 
    count += 1 # û�Ҹ� �������� 1 ���� 
    turn_time = 0 # ���� ���� ȸ�� Ƚ�� 0���� �ʱ�ȭ 
    continue # �ݺ� 
  else: # �̵��� �Ұ��� �� ��� ���� ���� ȸ��, Ƚ�� ���� 
    turn_time += 1 
  if turn_time == 4: # �� 4�� ȸ�� �� ���, �� ���� ��� û�Ұ� �Ǿ� �ְų� ���� �ִ� ��� 
    nx = x-dx[direction] # �ٶ󺸴� ���⿡�� �ڷ� �̵� 
    ny = y-dy[direction] # �ٶ󺸴� ���⿡�� �ڷ� �̵� 
    if array[nx][ny] == 0: #�̵��� ��ġ�� ���� �ƴ϶��, 
      x = nx # �̵� 
      y = ny # �̵� 
    else: # �׷��� ������, 
      break # �۵��� ���� 
    turn_time = 0 # ���� ���� ȸ�� Ƚ�� �ʱ�ȭ 
print(count) # count �� ���
