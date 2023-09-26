import sys
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(list):
  global ans
  visited = []
  total = 0
  for x, y in list:
    visited.append((x, y))
    total += fields[x][y]
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (nx, ny) not in visited:
        visited.append((nx, ny))
        total += fields[nx][ny]
      else:
        return
  ans = min(ans, total)

N = int(input())
ans = int(sys.maxsize)
fields = [list(map(int, input().split())) for _ in range(N)]
candidates = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]

for list in combinations(candidates, 3):
  check(list)
print(ans)