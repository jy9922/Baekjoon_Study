from itertools import combinations

team = int(input())
s = []
team_num = []
team_hap = 0
team_cha = []

for i in range(team):
  s.append(list(map(int, input().split())))

for i in range(team):
  team_num.append(i)

result = list(combinations(team_num,(team//2)))

def team_match(a,team_hap):
  team_person = list(combinations(a,2))
  for i in range(len(team_person)):
    x, y = team_person[i]
    team_hap += s[x][y] + s[y][x] 
  return team_hap
    
for i in range(len(result)//2):
  team_cha.append(abs(team_match(result[i],team_hap) - team_match(result[len(result)-i-1],team_hap)))

print(min(team_cha))
    
  
  