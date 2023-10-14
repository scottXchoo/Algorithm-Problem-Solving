from collections import deque

K = int(input())
arr = [int(input()) for _ in range(K)]

dq = deque()
for i in arr:
  if i != 0:
    dq.append(i)
  else:
    dq.pop()

ans = 0
for i in dq:
  ans += i

print(ans)