UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  r, c = r - 1, c - 1
  board[r][c] = (s, d, z)

def fish(j):
  for i in range(R):
    if board[i][j]:
      x = board[i][j][2]
      board[i][j] = 0
      return x
  return 0

def move():
  global board
  new_board = [[0 for _ in range(C)] for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if board[i][j]:
        ni, nj, nd = get_next_loc(i, j, board[i][j][0], board[i][j][1])
        if new_board[ni][nj]:
          new_board[ni][nj] = max(
            new_board[ni][nj],
            (board[i][j][0], nd, board[i][j][2]),
            key = lambda x: x[2] # z를 기준으로 max 찾기
          )
        else:
          new_board[ni][nj] = (board[i][j][0], nd, board[i][j][2])
  board = new_board

def get_next_loc(i, j, speed, dir):
  if dir == UP or dir == DOWN:
    cycle = 2 * R - 2
    if dir == UP:
      speed += cycle - i
    else:
      speed += i

    speed %= cycle
    if speed >= R:
      return (cycle - speed, j, UP)
    return (speed, j, DOWN)
  else:
    cycle = 2 * C - 2
    if dir == LEFT:
      speed += cycle - j
    else:
      speed += j

    speed %= cycle
    if speed >= C:
      return (i, cycle - speed, LEFT)
    return (i, speed, RIGHT)

ans = 0
for j in range(C):
  ans += fish(j)
  move()

print(ans)