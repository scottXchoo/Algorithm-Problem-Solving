from copy import deepcopy
N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().split())))

def move(board, dir):
  if dir == 0: # 동쪽
    for i in range(N):
      top = N - 1
      for j in range(N-2, -1, -1):
        if board[i][j]:
          tmp = board[i][j]
          board[i][j] = 0
          if board[i][top] == 0:
            board[i][top] = tmp
          elif board[i][top] == tmp:
            board[i][top] = tmp * 2
            top -= 1
          else:
            top -= 1
            board[i][top] = tmp     
  elif dir == 1: # 서쪽
    for i in range(N):
      top = 0
      for j in range(1, N):
        if board[i][j]:
          tmp = board[i][j]
          board[i][j] = 0
          if board[i][top] == 0:
            board[i][top] = tmp
          elif board[i][top] == tmp:
            board[i][top] = tmp * 2
            top += 1
          else:
            top += 1
            board[i][top] = tmp
  elif dir == 2: # 남쪽
    for j in range(N):
      top = N - 1
      for i in range(N-2, -1, -1):
        if board[i][j]:
          tmp = board[i][j]
          board[i][j] = 0
          if board[top][j] == 0:
            board[top][j] = tmp
          elif board[top][j] == tmp:
            board[top][j] = tmp * 2
            top -= 1
          else:
            top -= 1
            board[top][j] = tmp
  else:
    for j in range(N):
      top = 0
      for i in range(1, N):
        if board[i][j]:
          tmp = board[i][j]
          board[i][j] = 0
          if board[top][j] == 0:
            board[top][j] = tmp
          elif board[top][j] == tmp:
            board[top][j] = tmp * 2
            top += 1
          else:
            top += 1
            board[top][j] = tmp
  return board

def dfs(board, cnt):
  global ans
  if cnt == 5:
    for i in range(N):
      for j in range(N):
        ans = max(ans, board[i][j])
    return

  for i in range(4):
    tmp_board = move(deepcopy(board), i)
    dfs(tmp_board, cnt+1)

ans = 0
dfs(board, 0)
print(ans)