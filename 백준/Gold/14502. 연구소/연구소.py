'''
<문제 분석>
꼭 벽 3개를 다 세워야 된다.
안전 영역 : 바이러스(2)가 다 퍼진 뒤, 0의 개수
안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오

<제한 조건>
3 <= N, M <= 8
2 <= 바이러스(2) <= 10

<아이디어>
1. 주어진 map에 벽 3개를 세운다.
 - 3개는 조합으로 정한다.
2. 3개를 세운 뒤, 바이러스를 퍼뜨린다.
 - 바이러스의 위치도 필요하겠다.
3. 바이러스가 다 퍼진 벽에 있는 0의 개수를 세고 업데이트한다.
'''

from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

blanks, virus = [], []
for i in range(N):
  for j in range(M):
    if maps[i][j] == 0:
      blanks.append((i, j))
    if maps[i][j] == 2:
      virus.append((i, j))

def is_in_range(r, c):
  return 0 <= r < N and 0 <= c < M

def bfs(board):
  visited = [[0] * M for _ in range(N)]
  q = deque()
  for r, c in virus:
    q.append((r, c))
    visited[r][c] = 1
  
  while q:
    c_r, c_c = q.popleft()
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      n_r = c_r + dr
      n_c = c_c + dc
      if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
        if board[n_r][n_c] == 0:
          q.append((n_r, n_c))
          board[n_r][n_c] = 2
          visited[n_r][n_c] = 1

answer = 0
for combi in combinations(blanks, 3):
  cnt = 0
  temp = copy.deepcopy(maps)
  for i, j in combi:
    temp[i][j] = 1
  bfs(temp)
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        cnt += 1
  answer = max(answer, cnt)

print(answer)