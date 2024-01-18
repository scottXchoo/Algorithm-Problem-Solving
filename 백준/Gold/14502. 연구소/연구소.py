from itertools import combinations
from collections import deque
import copy

def bfs(r, c, map):
  visited = [[False] * M for _ in range(N)]
  dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

  q = deque()
  q.append((r, c))
  visited[r][c] = True
  while q:
    cur_r, cur_c = q.popleft()
    for i in range(4):
      next_r = cur_r + dr[i]
      next_c = cur_c + dc[i]
      if 0 <= next_r < N and 0 <= next_c < M and map[next_r][next_c] != 1:
        if not visited[next_r][next_c]:
          if map[next_r][next_c] == 0:
            map[next_r][next_c] = 2
            q.append((next_r, next_c))
            visited[next_r][next_c] = True

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

walls, virus = [], []
for i in range(N):
  for j in range(M):
    if maps[i][j] == 0:
      walls.append((i, j))
    if maps[i][j] == 2:
      virus.append((i, j))
    
answer = 0
for wall in combinations(walls, 3):
  cnt = 0
  temp = copy.deepcopy(maps)
  for i, j in wall:
    temp[i][j] = 1
  for r, c in virus:
    bfs(r, c, temp)
  for n in range(N):
    for m in range(M):
      if temp[n][m] == 0:
        cnt += 1
  answer = max(answer, cnt)

print(answer)