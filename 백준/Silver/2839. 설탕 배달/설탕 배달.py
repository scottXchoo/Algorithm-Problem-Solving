import sys
N = int(input())

ans = sys.maxsize
temp = 0

for i in range(0, N+1):
  for j in range(0, N+1):
    sum = 3*i + 5*j
    if sum == N:
      temp = i + j
      ans = min(ans, temp)

if temp == 0:
    print(-1)
else:
    print(ans)