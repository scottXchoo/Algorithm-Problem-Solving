import sys
import itertools
import collections

N = int(input())
## scvs가 3개가 아닌 1개나 2개 남았을 때, 처리하는 법
scvs = list(map(int, input().split())) + [0] * (3 - N)
## 3차원 배열의 visited
visited = [[[0 for i in range(61)]for j in range(61)]for k in range(61)]

## [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
combs = list(itertools.permutations([9, 3, 1], 3))
dq = collections.deque([[scvs, 0]])

while dq:
    tmp, cnt = dq.popleft()
    check = 0
    for i in range(3):
        if tmp[i] < 0:
            tmp[i] = 0
        ## 하나라도 체력이 남아있으면, break X
        if tmp[i] > 0:
            check = 1
    if check == 0:
        break
      
    for comb in combs:
        next_scv = [0] * 3
        for i in range(3):
            ## if tmp[i] - comp[i]가 0보다 크면, True(1)여서 'tmp[i] - comb[i]''
            ## else: False(0)여서 '0'
            next_scv[i] = [0, tmp[i] - comb[i]][tmp[i] - comb[i] > 0]
        if not visited[next_scv[0]][next_scv[1]][next_scv[2]]:
            # 3차원 배열의 visited가 0이 아니라면, 1로 바꿔주기
            visited[next_scv[0]][next_scv[1]][next_scv[2]] = 1
            dq.append([next_scv, cnt + 1])

print(cnt)