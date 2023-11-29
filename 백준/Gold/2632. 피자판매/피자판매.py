Target = int(input())
M, N = map(int, input().split())
a, b = [], []
for _ in range(M):
  a.append(int(input()))
for _ in range(N):
  b.append(int(input()))

a_comb, b_comb = [0] * (sum(a)+1), [0] * (sum(b)+1)
a_comb[0], b_comb[0] = 1, 1
a_comb[-1], b_comb[-1] = 1, 1

for j in range(1, M):
  for i in range(M):
    if i+j > M:
      sum_a = sum(a[i:] + a[:(i+j)%M])
    else:
      sum_a = sum(a[i:i+j])
    a_comb[sum_a] += 1

for j in range(1, N):
  for i in range(N):
    if i+j > N:
      sum_b = sum(b[i:] + b[:(i+j)%N])
    else:
      sum_b = sum(b[i:i+j])
    b_comb[sum_b] += 1

ans = 0
for i in range(Target+1):
  j = Target - i
  if 0 <= i < len(a_comb) and 0 <= j < len(b_comb):
    ans += a_comb[i] * b_comb[j]
print(ans)