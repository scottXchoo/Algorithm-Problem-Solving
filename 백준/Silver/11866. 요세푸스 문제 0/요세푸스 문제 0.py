import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
dq = deque(i for i in range(1, N + 1))
ans = []

while dq:
  for _ in range(K - 1):
    dq.append(dq.popleft())
  ans.append(str(dq.popleft()))

print('<' + ', '.join(ans) + '>')