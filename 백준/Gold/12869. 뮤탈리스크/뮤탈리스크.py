import sys
import itertools
import collections

N = int(input())
scvs = sorted(list(map(int, input().split())) + [0] * (3 - N))
visited = [[[0 for i in range(61)]for j in range(61)]for k in range(61)]
combs = list(itertools.permutations([9, 3, 1], 3))
dq = collections.deque([[scvs, 0]])

while dq:
    tmp, cnt = dq.popleft()
    if tmp[2] <= 0:
      break
      
    for comb in combs:
        next_scv = [0] * 3
        for i in range(3):
            next_scv[i] = [0, tmp[i] - comb[i]][tmp[i] - comb[i] > 0]
        next_scv.sort()
        if not visited[next_scv[0]][next_scv[1]][next_scv[2]]:
            visited[next_scv[0]][next_scv[1]][next_scv[2]] = 1
            dq.append([next_scv, cnt + 1])

print(cnt)
