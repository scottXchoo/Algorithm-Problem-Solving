from collections import deque

R, C = map(int, input().split())
ex, ey, ans = 0, 0, 0 # ex, ey는 두 번째 백조의 위치 & ans는 날짜
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
graph = [list(input().strip()) for _ in range(R)]
wv, sv = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

def water():
  while wq1:
    x, y = wq1.popleft()
    graph[x][y] = '.'
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not(0 <= nx < R and 0 <= ny < C) or wv[nx][ny] == 1:
        continue
      if graph[nx][ny] == ".": # 물이 있다면, wq1에 추가
        wq1.append((nx, ny))
      else: # 물이 없다면, wq2에 추가
        wq2.append((nx, ny))
      wv[nx][ny] = 1

def swan():
  while sq1:
    x, y = sq1.popleft()
    if x == ex and y == ey: # 백조가 만난 순간!
      return True
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not(0 <= nx < R and 0 <= ny < C) or sv[nx][ny] == 1:
        continue
      if graph[nx][ny] == ".":
        sq1.append((nx, ny))
      else:
        sq2.append((nx, ny))
      sv[nx][ny] = 1

for i in range(R):
  for j in range(C):
    if graph[i][j] == "L":
      if not sq1: # 첫 번째 백조
        sq1.append((i, j))
        sv[i][j] = 1
      else:
        ex, ey = i, j # 두 번째 백조
      graph[i][j] = "."
    if graph[i][j] == ".":
      wq1.append((i, j))
      wv[i][j] = 1

while True:
  water() # 쫙 녹여라~
  if swan(): # 백조끼리 만났으면 끝
    break
  wq1, sq1 = wq2, sq2 # 다음 날이 되어 업데이트
  wq2, sq2 = deque(), deque() # 새로운 값을 넣어주기 위해 초기화
  ans += 1 # 날짜 초과

print(ans)