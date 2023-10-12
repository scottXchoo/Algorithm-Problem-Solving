N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check(line, L):
  visited = [False for _ in range(N)]
  for i in range(0, N-1):
    if line[i] == line[i+1]: # 숫자 연속 : 1'11'2
      continue
    elif abs(line[i] - line[i+1]) > 1: # 높이 차이가 1보다 클 때 : 1'13'3
      return False
    elif line[i] > line[i+1]: # 내리막 : 2'21'1
      temp = line[i+1]
      for j in range(i+1, i+L+1): # 기준 + 1 ~ 기준 + L까지 체크 : 2'211'2
        if not(0 <= j < N): # 범위 포함 X
          return False
        else:
          if temp != line[j]: # L만큼 연속 X
            return False
          elif visited[j]: # 이미 방문함
            return False
          visited[j] = True

    else:
      temp = line[i]
      for j in range(i, i-L, -1): # 오르막 : 11'12'3
        if not(0 <= j < N): # 범위 포함 X
          return False
        else:
          if temp != line[j]: # L만큼 연속 X
            return False
          elif visited[j]: # 이미 방문함
            return False
          visited[j] = True

  return True

# 가로 탐색
for map in maps:
  if check(map, L):
    ans += 1

# 세로 탐색
for i in range(N):
  temp = []
  for j in range(N):
    temp.append(maps[j][i])
  if check(temp, L):
    ans += 1

print(ans)    