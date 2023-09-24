R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
  global ans
  ans = max(ans, cnt)
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if not(0 <= nx < R and 0 <= ny < C):
      continue
    # 만약 alphas 안에 해당 알파벳이 없으면
    if maps[nx][ny] not in alphas:
      ## alphas 안에 해당 알파벳을 넣고
      alphas.add(maps[nx][ny])
      ## 깊숙하게 dfs로 들어가서 cnt를 계속 올려준다
      dfs(nx, ny, cnt + 1)
      ## 백트래킹 : 그러다 dfs가 끝나서 다시 처음으로 돌아오기 위해 해당 알파벳을 제거함으로써 초기화시킨다
      alphas.remove(maps[nx][ny])

alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)
