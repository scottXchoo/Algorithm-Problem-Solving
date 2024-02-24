from collections import deque
import sys

# 백준 입력 형식
N, M = map(int, input().split())
board = []
rr, rc, br, bc = 0, 0, 0, 0
for i in range(N):
  board.append(list(input()))
  for j in range(M):
    if board[i][j] == 'R': # 빨간구슬 위치
      rr, rc = i, j
    if board[i][j] == 'B': # 파란구슬 위치
      br, bc = i, j

def move(r, c, dr, dc):
  cnt = 0
  nr, nc = r, c
  while True:
    prev_nr, prev_nc = nr, nc
    nr += dr
    nc += dc
    cnt += 1
    if board[nr][nc] == "#":
      return prev_nr, prev_nc, cnt
    elif board[nr][nc] == "O":
      return nr, nc, cnt

answer = 0

dq = deque()
dq.append((rr, rc, br, bc, 1))

visited = set()
visited.add((rr, rc, br, bc))

while dq:
  c_rr, c_rc, c_br, c_bc, level = dq.popleft()
  if level > 10:
    break
  for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    n_rr, n_rc, r_cnt = move(c_rr, c_rc, dr, dc)
    n_br, n_bc, b_cnt = move(c_br, c_bc, dr, dc)
    if board[n_br][n_bc] == "O":
      continue
    if (n_rr, n_rc, n_br, n_bc) not in visited:
      if (n_rr == n_br) and (n_rc == n_bc):
        if r_cnt > b_cnt:
          n_rr -= dr
          n_rc -= dc
        else:
          n_br -= dr
          n_bc -= dc
      if board[n_rr][n_rc] == "O":
        answer = 1
        break
      dq.append((n_rr, n_rc, n_br, n_bc, level+1))
      visited.add((n_rr, n_rc, n_br, n_bc))
  else:
    continue
  break

print(answer)