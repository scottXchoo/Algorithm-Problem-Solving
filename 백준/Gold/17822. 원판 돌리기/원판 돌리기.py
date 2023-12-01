from collections import deque

N, M, T = map(int, input().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

def rotate(x, d, k):
  dq = deque()
  dq.extend(graph[x])
  if d == 0: # 시계방향
    dq.rotate(k)
  else:
    dq.rotate(-k)
  graph[x] = list(dq)

def change_avg():
  avg_cnt, all_sum = 0, 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] != 0:
        avg_cnt += 1
        all_sum += graph[i][j]
  if avg_cnt == 0:
    return False
  avg = all_sum / avg_cnt
  for i in range(N):
    for j in range(M):
      if graph[i][j] != 0:
        if graph[i][j] > avg:
          graph[i][j] -= 1
        elif graph[i][j] < avg:
          graph[i][j] += 1
  return True

def solve(x, y):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = 1
  value = graph[x][y]
  graph[x][y] = 0
  cnt = 0
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not (0 <= ny < M):
        if y == 0:
          ny = M-1
        elif y == M-1:
          ny = 0
      if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
        continue
      if graph[nx][ny] == value:
        cnt += 1
        graph[nx][ny] = 0
        dq.append((nx, ny))
        visited[nx][ny] = 1
  if cnt == 0:
    graph[x][y] = value
  return cnt

for _ in range(T):
  x, d, k = map(int, input().split())
  check_sum = 0
  for i in range(N):
    check_sum += sum(graph[i])
    if (i+1) % x == 0:
      rotate(i, d, k)
  if check_sum == 0:
    break
  else:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
      for j in range(M):
        if not visited[i][j] and graph[i][j] != 0:
          cnt += solve(i, j)
    if cnt == 0:
      change_avg()

ans = 0
for i in range(N):
  ans += sum(graph[i])

print(ans)