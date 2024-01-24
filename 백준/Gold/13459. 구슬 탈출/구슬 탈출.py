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
  while True:
    r += dr
    c += dc
    pre_r = r - dr
    pre_c = c - dc
    cnt += 1
    if board[r][c] == "#":
      return pre_r, pre_c, cnt
    if board[r][c] == "O":
      return r, c, cnt

answer = 0
queue = deque()
visited = set()

queue.append([rr, rc, br, bc, 0])
visited.add((rr, rc, br, bc))

while queue:
  c_rr, c_rc, c_br, c_bc, cnt = queue.popleft()
  if cnt >= 10:
    break
  for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]: # 오른, 아래, 왼, 위
    n_rr, n_rc, r_d = move(c_rr, c_rc, dr, dc)
    n_br, n_bc, b_d = move(c_br, c_bc, dr, dc)
    if board[n_br][n_bc] == "O":
      continue
    if (n_rr, n_rc, n_br, n_bc) in visited:
      continue
    if board[n_rr][n_rc] == "O":
      answer = 1
      break
    if n_rr == n_br and n_rc == n_bc: # 빨간공과 파란공 같은 위치일 때
      if r_d >= b_d: # 빨간공이 더 뒤에 있었다는 얘기
        n_rr -= dr
        n_rc -= dc
      else: # 파란공이 더 뒤에 있었다는 얘기
        n_br -= dr
        n_bc -= dc
    queue.append([n_rr, n_rc, n_br, n_bc, cnt+1])
    visited.add((n_rr, n_rc, n_br, n_bc))
  else:
    continue
  break

print(answer)