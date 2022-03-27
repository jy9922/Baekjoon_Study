import sys
k = int(sys.stdin.readline())
rope = []
w = []

for i in range(k):
  rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)

result = 0
for i in range(k):
  weight = rope[i] * (i+1)
  if weight >= result:
    result = weight
print(result)

