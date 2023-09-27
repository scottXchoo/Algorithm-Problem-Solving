R, C, K = map(int, input().split())
graph = [list(input()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
graph[R-1][0] = 'T'

def dfs(x, y, cnt):
  global ans
  if (x, y) == (0, C - 1) and cnt == K:
    ans += 1
  else:
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not(0 <= nx < R and 0 <= ny < C) or graph[nx][ny] == 'T':
        continue
      graph[nx][ny] = 'T'
      dfs(nx, ny, cnt + 1)
      graph[nx][ny] = '.'

dfs(R - 1, 0, 1)
print(ans)