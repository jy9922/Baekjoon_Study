n = int(input())
liquid = list(map(int, input().split()))

liquid = sorted(liquid, key = abs)
result = abs(liquid[1] + liquid[0])
ax, ay = liquid[0], liquid[1]

for i in range(1, n):
  if i == n-1:
    break

  cha = abs(liquid[i] + liquid[i+1])
  if result > cha:
    result = cha
    ax, ay = liquid[i], liquid[i+1] 

if ax <= ay:
  print(ax, ay)
else:
  print(ay, ax)
  
