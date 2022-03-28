n = int(input())
turn = 2 * n - 1
result = 1
result_new = turn

for i in range(1, turn+1):
  if i <= n:
    print(' ' * (n-i),end='')
    print('*' * result)
    result += 2
  else:
    result_new -= 2
    print(' ' * (i-n),end='')
    print('*' * result_new)