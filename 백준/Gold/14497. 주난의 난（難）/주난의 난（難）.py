from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = []
for _ in range(N):
  # input().split()이면, list index out of range
  graph.append(list(map(str, input().rstrip())))

distance = [[-1] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  distance[x][y] = 0

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not(0 <= nx < N and 0 <= ny < M):
        continue
      if distance[nx][ny] == -1:
        if graph[nx][ny] == "1" or graph[nx][ny] == "#":
          distance[nx][ny] = distance[x][y] + 1
          dq.append((nx, ny))
        elif graph[nx][ny] == "0":
          # distance 값은 시작한 곳과 같이 그대로 간다.
          distance[nx][ny] = distance[x][y]
          # "1"과 "#"가 아니기에 바로바로 탐색을 위해 appendleft!!!
          dq.appendleft((nx, ny))

bfs(x1 - 1, y1 - 1)
print(distance[x2 - 1][y2 - 1])