import sys

n, k = list(map(int, sys.stdin.readline().split()))
sun = []
for i in range(n):
  sun.append(int(sys.stdin.readline()))
start = 1
end = max(sun)

result = 0
while (start <= end):
  sun_total = 0
  mid = (start + end) // 2
  for x in sun:
    if x >= mid:
      sun_total += x // mid
  if sun_total < k:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
    
print(result)
      