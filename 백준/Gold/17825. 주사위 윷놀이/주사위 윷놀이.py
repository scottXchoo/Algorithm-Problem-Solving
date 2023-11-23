graph = [[1], [2], [3], [4], [5],
   [6, 21], [7], [8], [9], [10],
   [11, 25], [12], [13], [14], [15],
   [16, 27], [17], [18], [19], [20],
   [32], [22], [23], [24], [30],
   [26], [24], [28], [29], [24],
   [31], [20], [32]]

score = [0, 2, 4, 6, 8,
   10, 12, 14, 16, 18,
   20, 22, 24, 26, 28,
   30, 32, 34, 36, 38,
   40, 13, 16, 19, 25,
   22, 24, 28, 27, 26,
   30, 35, 0]

dice = list(map(int, input().split()))
ans = 0

def backtracking(depth, result, horses):
  global ans
  if depth == 10:
    ans = max(ans, result)
    return

  for i in range(4):
    x = horses[i] # 현재 말 위치
    
    # 현재 말 위치가 두 갈래 갈 수 있는 위치(10, 20, 30)인지 체크
    if len(graph[x]) == 2:
      # 파란 길 한 칸 진입
      x = graph[x][1]
    else:
      # 빨간 길 한 칸 진입
      x = graph[x][0]

    # 나온 주사위 값만큼 말 이동 (위에서 1칸 이동했기 때문에 1 덜 이동)
    for _ in range(1, dice[depth]):
      x = graph[x][0]

    # 목적지에 도착했거나 or (아직 목적지가 아니고 and 거기에 말이 없다면)
    if x == 32 or (x < 32 and x not in horses):
      before = horses[i] # 이전 말의 위치
      horses[i] = x # 현재 말 위치 갱신

      backtracking(depth+1, result+score[x], horses)

      horses[i] = before

backtracking(0, 0, [0, 0, 0, 0])
print(ans)