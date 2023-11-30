from collections import deque

Target = int(input())
M, N = map(int, input().split())
a, b = [], []
for _ in range(M):
  a.append(int(input()))
for _ in range(N):
  b.append(int(input()))

def get_cnt(arr, m):
  cnt_arr = [0] * (sum(arr) + 1)
  cnt_arr[0], cnt_arr[-1] = 1, 1
  for i in range(m):
    dq = deque(arr)
    for _ in range(i):
      dq.rotate(-1)
    dq.pop()
    summ = 0
    while dq:
      summ += dq.popleft()
      cnt_arr[summ] += 1
  return cnt_arr

cnt_a = get_cnt(a, M)
cnt_b = get_cnt(b, N)
ans = 0
for i in range(Target+1):
  j = Target - i
  if 0 <= i < len(cnt_a) and 0 <= j < len(cnt_b):
    ans += cnt_a[i] * cnt_b[j]
      
print(ans)
