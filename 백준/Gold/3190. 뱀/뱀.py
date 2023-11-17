from collections import deque

N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
  row, col = map(int, input().split())
  graph[row - 1][col - 1] = 2

L = int(input())
dirDict = dict()
for _ in range(L):
  x, c = input().split()
  dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cnt, direct = 0, 0
dq = deque()
dq.append((0, 0))


def turn(c):
  global direct
  if c == 'L':
    direct = (direct - 1) % 4
  else:
    direct = (direct + 1) % 4


while True:
  cnt += 1
  x += dx[direct]
  y += dy[direct]
  if x < 0 or x >= N or y < 0 or y >= N:
    break

  if graph[x][y] == 2:
    graph[x][y] = 1
    dq.append((x, y))
    if cnt in dirDict:
      turn(dirDict[cnt])

  elif graph[x][y] == 0:
    graph[x][y] = 1
    dq.append((x, y))
    tx, ty = dq.popleft()
    graph[tx][ty] = 0
    if cnt in dirDict:
      turn(dirDict[cnt])

  else:
    break

print(cnt)