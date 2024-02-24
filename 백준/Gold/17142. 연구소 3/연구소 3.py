from itertools import combinations
from collections import deque
import sys

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
virus = []
board = [["_"] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if maps[i][j] == 2:
      virus.append((i, j))
      board[i][j] = "*"
    elif maps[i][j] == 1:
      board[i][j] = "-"

def is_in_range(r, c):
  return 0 <= r < N and 0 <= c < N

def bfs(virus, map):
  max_time = 0
  dq = deque()
  for r, c in virus:
    dq.append((r, c, 0))
    map[r][c] = 0

  while dq:
    c_r, c_c, time = dq.popleft()
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      n_r = c_r + dr
      n_c = c_c + dc
      n_time = time + 1
      if is_in_range(n_r, n_c):
        if map[n_r][n_c] == "_": # 빈 칸이면?
          dq.append((n_r, n_c, n_time))
          map[n_r][n_c] = n_time
          max_time = max(max_time, n_time)
        elif map[n_r][n_c] == "*": # 비활성이면?
          dq.append((n_r, n_c, n_time))
          map[n_r][n_c] = n_time

  for i in range(N):
    for j in range(N):
      if map[i][j] == "_":
        return -1
  else:
    return max_time    

answer = sys.maxsize
for active_virus in combinations(virus, M):
  temp = [item[:] for item in board]
  time = bfs(active_virus, temp)
  if time != -1:
    answer = min(answer, time)

if answer == sys.maxsize:
  print(-1)
else:
  print(answer)