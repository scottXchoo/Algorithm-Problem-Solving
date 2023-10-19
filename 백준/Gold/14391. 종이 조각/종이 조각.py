N, M = map(int, input().split())
paper = [list(map(int, input())) for _ in range(N)]
ans = []

for i in range(1 << N*M):
  total = 0
  for row in range(N):
    row_sum = 0
    for col in range(M):
      idx = row * M + col
      if i & (1 << idx) != 0:
        row_sum = row_sum * 10 + paper[row][col]
      else:
        total += row_sum
        row_sum = 0
    total += row_sum

  for col in range(M):
    col_sum = 0
    for row in range(N):
      idx = row * M + col
      if i & (1 << idx) == 0:
        col_sum = col_sum * 10 + paper[row][col]
      else:
        total += col_sum
        col_sum = 0
    total += col_sum
  ans.append(total)

print(max(ans))