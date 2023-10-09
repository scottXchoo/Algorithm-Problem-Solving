N = int(input())
coin = [list(input()) for _ in range(N)]
ans = N * N + 1

for bit in range(1 << N):
  tmp = [coin[i][:] for i in range(N)]
  for i in range(N):
    if bit & (1 << i):
      for j in range(N):
        if tmp[i][j] == "H":
          tmp[i][j] = "T"
        else:
          tmp[i][j] = "H"

  tsum = 0
  for i in range(N):
    cnt = 0
    for j in range(N):
      if tmp[j][i] == "T":
        cnt += 1
    tsum += min(cnt, N - cnt)
  ans = min(ans, tsum)

print(ans)