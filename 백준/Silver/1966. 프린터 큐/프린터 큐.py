from collections import deque
import sys

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  dq = deque(list(map(int, input().split())))
  idx_dq = deque(list(range(N)))
  cnt = 0
  
  while dq:
    if dq[0] == max(dq):
      dq.popleft()
      pop_idx = idx_dq.popleft()
      cnt += 1
      if pop_idx == M:
        print(cnt)

    else:
      dq.append(dq.popleft())
      idx_dq.append(idx_dq.popleft())