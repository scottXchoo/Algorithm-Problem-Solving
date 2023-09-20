import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

visited = [0] * 100001
route = [0] * 100001

def path(x):
  arr = []
  temp = x
  # 시작점까지 포함해야하기 때문에 "+ 1"
  for _ in range(visited[x] + 1):
    # 현재의 값을 arr에 넣고 그 위치에 할당된 값을 temp로 정의
    ## 이렇게 되면, 계속 역으로 시작점까지 가게 된다.
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
	      # 전의 값을 현재 위치에 할당할 수 있음
        route[nx] = x

print(bfs(n))
print(*path(k))
