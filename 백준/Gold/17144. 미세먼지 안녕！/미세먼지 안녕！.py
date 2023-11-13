R, C, T = map(int, input().split())
board, cleaner = [], []
for i in range(R):
  board.append(list(map(int, input().split())))
  for j in range(len(board[i])):
    if board[i][j] == -1:
      cleaner.append((i, j))


def dust_diffusion():
  steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  diffusion = [[0] * C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if not (board[i][j] == 0 or board[i][j] == -1):
        turn = 0
        for dx, dy in steps:
          nx, ny = i + dx, j + dy
          if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in cleaner:
            turn += 1
            diffusion[nx][ny] += board[i][j] // 5
        # 미세먼지가 주변으로 날라가고 남은 값을 업데이트함
        board[i][j] = board[i][j] - ((board[i][j] // 5) * turn)
  # board[i][j]는 현재 미세먼지가 주변에 날라가고 남은 값만 있어서
  # 다른 곳에서 날라온 미세먼지를 더해주기
  for i in range(R):
    for j in range(C):
      board[i][j] += diffusion[i][j]


def dust_clean_up():
  up_step = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 동, 북, 서, 남
  direct = 0
  x, y = cleaner[0]  # 위쪽 공기청정기
  up, y, prev = x, 1, 0  # 시작 위치
  while True:
    if x == up and y == 0:
      break
    nx, ny = x + up_step[direct][0], y + up_step[direct][1]
    if nx < 0 or nx >= R or ny < 0 or ny >= C:
      direct += 1  # 맵을 벗어나면, 방향을 바꿔주기 Ex) 동 -> 북
      continue
    board[x][y], prev = prev, board[x][y]
    x, y = nx, ny
  return


def dust_clean_down():
  down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동, 남, 서, 북
  direct = 0
  x, y = cleaner[1]  # 아래쪽 공기청정기
  down, y, prev = x, 1, 0  # 시작 위치
  while True:
    if x == down and y == 0:
      break
    nx, ny = x + down_step[direct][0], y + down_step[direct][1]
    if nx < 0 or nx >= R or ny < 0 or ny >= C:
      direct += 1  # 맵을 벗어나면, 방향을 바꿔주기 Ex) 동 -> 남
      continue
    board[x][y], prev = prev, board[x][y]
    x, y = nx, ny
  return


for _ in range(T):
  dust_diffusion()
  dust_clean_up()
  dust_clean_down()

ans = 0
for i in range(R):
  for j in range(C):
    if board[i][j] > 0:
      ans += board[i][j]

print(ans)
