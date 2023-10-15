from collections import deque
from itertools import combinations

N = int(input())
## [0, 5, 2, 3, 4, 1, 2]
people = [0] + list(map(int, input().split())) # 인구수
## [0, 0, 0, 0, 0, 0, 0]
link = [0 for _ in range(N + 1)] # 연결된 노드수
ans = float('inf')

for i in range(1, N + 1):
  ## [0, [2, 2, 4], [4, 1, 3, 6, 5], [2, 4, 2], [2, 1, 3], [1, 2], [1, 2]]
  link[i] = list(map(int, input().split()))
  ## [0, [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]
  link[i] = link[i][1:]

def bfs(comb): # comb = (1, 2, 4)
  global people, link
  start = comb[0] # start = 1
  dq = deque([start]) # dq = deque([1])
  visited = set([start]) # visited = {1}
  num = 0

  while dq:
    value = dq.popleft() # value = 1
    num += people[value]
    for i in link[value]: # i = 2, 4
      if i not in visited and i in comb:
        dq.append(i)
        visited.add(i)
  return num, len(visited)

for i in range(1, N // 2 + 1):
  ## [(1), (2), ...], [(1, 2), (1, 3), ...], [(1, 2, 3), (1, 2, 4), ...] ...
  combs = list(combinations(range(1, N + 1), i))
  ## (1, ), (2, ), ... (1, 2), (1, 3), ... (1, 2, 3), (1, 2, 4), ...
  for comb in combs:
    # 조합의 절반씩 계산
    sum1, node1 = bfs(comb)
    sum2, node2 = bfs([i for i in range(1, N + 1) if i not in comb])
    # [Wow] 끊기지 않고 다 연결이 될 때를 이렇게 표현할 수 있음
    if node1 + node2 == N:
      ans = min(ans, abs(sum1 - sum2))

if ans != float('inf'):
  print(ans)
else:
  print(-1)
