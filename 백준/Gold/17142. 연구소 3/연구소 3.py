from itertools import combinations
from collections import deque
import copy, sys

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
virus = []
answer = sys.maxsize

for r in range(N):
  for c in range(N):
    if maps[r][c] == 2:
      virus.append([r, c])
      maps[r][c] = "*"
    elif maps[r][c] == 1:
      maps[r][c] = "-"
    elif maps[r][c] == 0:
      maps[r][c] = "_"

def is_range(next_r, next_c):
  return 0 <= next_r < N and 0 <= next_c < N

def bfs(v):
  global answer
  dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
  q = deque()
  for r, c in v:
    q.append([r, c, 0])
  temp = copy.deepcopy(maps) # [board[i][:] for i in range(N)]
  max_time = 0
  
  while q:
    cur_r, cur_c, cur_t = q.popleft()
    for i in range(4):
      next_r = cur_r + dr[i]
      next_c = cur_c + dc[i]
      next_t = cur_t + 1
      if is_range(next_r, next_c):
        if temp[next_r][next_c] == "_":
          temp[next_r][next_c] = next_t
          max_time = max(max_time, next_t)
          q.append([next_r, next_c, next_t])
        elif temp[next_r][next_c] == "*":
          temp[next_r][next_c] = next_t
          q.append([next_r, next_c, next_t])

  # 바이러스가 다 퍼졌는데도 "_"가 있으면, answer 그대로
  for r in range(N):
    for c in range(N):
      if temp[r][c] == "_":
        return
  # 바이러스가 잘 퍼졌으면, answer 업데이트
  answer = min(answer, max_time)
  return

# 활성화될 바이러스 선택
for v in combinations(virus, M):
  for r, c in v:
    maps[r][c] = 0
  bfs(v)
  for r, c in v:
    maps[r][c] = "*"

if answer == sys.maxsize:
  answer = -1

print(answer)