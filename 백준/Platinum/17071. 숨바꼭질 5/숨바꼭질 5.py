from collections import deque

MAX_NUM = 500000
n, k = map(int, input().split())

# visited[0][n] : 짝수 시간에 위치 n을 방문한 최소시간
# visited[1][n] : 홀수 시간에 위치 n을 방문한 최소시간
visited = [[-1 for _ in range(MAX_NUM + 1)] for _ in range(2)]

def bfs(n):
  dq = deque()
  dq.append((n, 0))
  visited[0][n] = 0

  while dq:
    n, cnt = dq.popleft()
    isEven = cnt % 2

    for nx in [n+1, n-1, 2*n]:
      if 0 <= nx <= MAX_NUM and visited[1 - isEven][nx] == -1:
        # nx 위치는 cnt+1 시간에 방문하기 때문에
        # 시간이 홀짝 바뀌므로 1-isEven으로 변경
        visited[1 - isEven][nx] = cnt + 1
        dq.append((nx, cnt + 1))

# 먼저 가능한 모든 점 방문하기
bfs(n)

# k를 늘려보면서 이 점에 방문할 수 있는지 확인하기
t = 0
flag = 0
res = -1
while k <= MAX_NUM:
  if (visited[flag][k] != -1) and (visited[flag][k] <= t):
    res = t
    break
  flag = 1 - flag
  t += 1
  k += t

print(res)