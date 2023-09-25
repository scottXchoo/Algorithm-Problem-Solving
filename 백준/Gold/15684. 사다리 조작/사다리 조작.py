def check():
  for i in range(N):
    temp = i
    for j in range(H):
      if graph[j][temp]:
        temp += 1
      elif temp > 0 and graph[j][temp - 1]:
        temp -= 1
    if temp != i:
      return False
  return True

def dfs(x, y, cnt):
  global ans
  # 가로선을 정답보다 
  if ans <= cnt:
    return
  if check():
    ans = min(ans, cnt)
    return

  for i in range(x, H):
    k = y if i == x else 0
    for j in range(k, N - 1):
      if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i, j + 2, cnt + 1)
        graph[i][j] = 0

# main
## N : 세로, M : 가로, H : 세로선마다 가로선 놓을 수 있는 위치 수
N, M, H = map(int, input().split())
graph = [[0] * N for _ in range(H)]
for _ in range(M):
  a, b = map(int, input().split())
  ## 가로선, 세로선
  graph[a-1][b-1] = 1

ans = 4
dfs(0, 0, 0)
print(ans if ans <= 3 else -1)