n = int(input())
ban = list(map(int, input().split()))
b,c = map(int, input().split())

total = 0
result = []

for i in ban:
  total = 0
  remain = i - b
  total += 1
  if remain > 0:
    total += remain // c
    if remain % c != 0:
      total += 1
  result.append(total)

print(sum(result))
  