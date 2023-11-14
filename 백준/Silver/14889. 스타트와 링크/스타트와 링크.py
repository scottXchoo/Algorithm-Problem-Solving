import sys
N = int(input())
visited = [False for _ in range(N)]
tables = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize


def backTracking(depth, idx):
  global ans
  if depth == N // 2:
    start, link = 0, 0
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]:
          start += tables[i][j]
        elif not visited[i] and not visited[j]:
          link += tables[i][j]
    ans = min(ans, abs(start - link))
    return
  for i in range(idx, N):
    if not visited[i]:
      visited[i] = True
      backTracking(depth + 1, i + 1)
      visited[i] = False


backTracking(0, 0)
print(ans)