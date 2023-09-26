# 풀이 1. DFS & 백트래킹
import sys

N = int(input())
fields = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = int(sys.maxsize)

def check(x, y, visited):
  for i in range(5):
    nx, ny = x + dx[i], y + dy[i]
    if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny] == 1:
      return False
  return True

def calc(x, y):
  cost = 0
  for i in range(5):
    nx, ny = x + dx[i], y + dy[i]
    cost += fields[nx][ny]
  return cost

def dfs(cnt, visited, cost_sum):
  global ans
  if cnt == 3:
    ans = min(ans, cost_sum)
    return

  for x in range(1, N-1):
    for y in range(1, N-1):
      if check(x, y, visited):
        for i in range(5):
          nx, ny = x + dx[i], y + dy[i]
          visited[nx][ny] = 1
        
        dfs(cnt+1, visited, cost_sum + calc(x, y))
        
        for i in range(5):
          nx, ny = x + dx[i], y + dy[i]
          visited[nx][ny] = 0

dfs(0, visited, 0)
print(ans)

# 풀이 2. 조합(combination) 이용
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

# 풀이 3. 재귀함수 이용
import sys

def check(x, y):
  for i in range(5):
    nx, ny = x + dx[i], y + dy[i]
    if visited[nx][ny] == 1:
      return False
  return True

def recur(cur):
  global total, ans

  if cur == 3:
    ans = min(ans, total)
    return

  for x in range(1, N-1):
    for y in range(1, N-1):
      if check(x, y):
        for i in range(5):
          nx, ny = x + dx[i], y + dy[i]
          visited[nx][ny] = 1
          total += fields[nx][ny]

        recur(cur + 1)

        for i in range(5):
          nx, ny = x + dx[i], y + dy[i]
          visited[nx][ny] = 0
          total -= fields[nx][ny]
          
N = int(input())
fields = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
ans = int(sys.maxsize)
total = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

recur(0)
print(ans)
