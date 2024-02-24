from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

blanks, virus = [], []
for i in range(N):
  for j in range(M):
    if maps[i][j] == 0:
      blanks.append((i, j))
    elif maps[i][j] == 2:
      virus.append((i, j))

def is_in_range(r, c):
  return 0 <= r < N and 0 <= c < M

def bfs(map):
  cnt = 0
  visited = [[0] * M for _ in range(N)]
  dq = deque()
  for i, j in virus:
    dq.append((i, j))
    visited[i][j] = 1

  while dq:
    c_r, c_c = dq.popleft()
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      n_r = c_r + dr
      n_c = c_c + dc
      if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
        if map[n_r][n_c] == 0:
          dq.append((n_r, n_c))
          map[n_r][n_c] = 2
          visited[n_r][n_c] = 1

  for i in range(N):
    for j in range(M):
      if map[i][j] == 0:
        cnt += 1

  return cnt
  
answer = 0
for combi in combinations(blanks, 3):
  temp = [map[:] for map in maps]
  for i, j in combi:
    temp[i][j] = 1
  cnt = bfs(temp)
  answer = max(answer, cnt)

print(answer)