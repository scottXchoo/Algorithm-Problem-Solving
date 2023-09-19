import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

visited = [0] * 100001
route = [0] * 100001

def path(x):
  arr = []
  temp = x
  for _ in range(visited[x] + 1):
    arr.append(temp)
    temp = route[temp]
  return arr[::-1]

def bfs(x):
  dq = deque()
  dq.append(x)
  while dq:
    x = dq.popleft()
    if x == k:
      return visited[x]
    for nx in [x-1, x+1, 2*x]:
      if 0 <= nx < 100001 and visited[nx] == 0:
        dq.append(nx)
        visited[nx] = visited[x] + 1
        route[nx] = x

print(bfs(n))
print(*path(k))