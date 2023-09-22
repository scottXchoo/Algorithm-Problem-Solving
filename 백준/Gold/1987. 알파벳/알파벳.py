r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
  global ans
  ans = max(ans, cnt)
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] not in alphas:
      alphas.add(maps[nx][ny])
      dfs(nx, ny, cnt + 1)
      alphas.remove(maps[nx][ny])

alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)