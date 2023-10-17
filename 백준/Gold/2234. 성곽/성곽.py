from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
room_cnt, room_size = 0, 0
visited = [[False] * N for _ in range(M)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = True
  room = 1

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      if maps[x][y] & (1 << i) == 0:
        nx, ny = x + dx[i], y + dy[i]

        if not(0 <= nx < M and 0 <= ny < N):
          break
          
        if visited[nx][ny] == False:
          dq.append((nx, ny))
          visited[nx][ny] = True
          room += 1
  return room

for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      room_cnt += 1
      room_size = max(room_size, bfs(i, j))

print(room_cnt)
print(room_size)

room_del = 0
for i in range(M):
  for j in range(N):
    for k in range(4):
      if maps[i][j] & (1 << k) == (1 << k):
        visited = [[False] * N for _ in range(M)]
        maps[i][j] -= (1 << k)
        room_del = max(room_del, bfs(i, j))
        maps[i][j] += (1 << k)

print(room_del)