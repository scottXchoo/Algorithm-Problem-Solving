N = int(input())
maps = [[0] * 101 for _ in range(101)]
dx, dy = [(1, 0, -1, 0), (0, -1, 0, 1)]
for _ in range(N):
  x, y, d, g = map(int, input().split())
  maps[x][y] = 1

  curves = [d]
  for j in range(g):
    for k in range(len(curves) - 1, -1, -1):
      curves.append((curves[k] + 1) % 4) # 0, 1, 2, 1 => 2, 3, 2, 1

  for curve in curves:
    x += dx[curve]
    y += dy[curve]
    if x < 0 or x >= 101 or y < 0 or y >= 101:
      continue
    maps[x][y] = 1

def get_count():
  global maps
  cnt = 0
  for i in range(100):
    for j in range(100):
      if maps[i][j] and maps[i+1][j] and maps[i][j+1] and maps[i+1][j+1]:
        cnt += 1
  return cnt

ans = 0
for i in range(N):
  ans = get_count()

print(ans)