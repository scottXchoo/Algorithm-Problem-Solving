import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
idx = 0
max_h = 0

for i in range(N):
  for j in range(M):
    if maps[i][j] > max_h:
      max_h = maps[i][j]

for target in range(max_h + 1):
  max_target, min_target = 0, 0

  for i in range(N):
    for j in range(M):
      if maps[i][j] >= target:
        # target보다 map이 더 크니까 블록 제거
        max_target += maps[i][j] - target
      else:
        # target보다 map이 더 작으니까 블록 추가
        min_target += target - maps[i][j]

  if (max_target + B >= min_target) and ((min_target + (max_target * 2)) <= ans):
    ans = min_target + (max_target * 2)
    idx = target

print(ans, idx)