from collections import deque

N, M, G = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
t_r, t_c = map(int, input().split())
t_r -= 1
t_c -= 1

fuel = G
answer = -1
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
passenger = {}
for _ in range(M):
  pr, pc, pdr, pdc = map(int, input().split())
  passenger[(pr-1, pc-1)] = (pdr-1, pdc-1)

def is_in_range(r, c):
  return 0 <= r < N and 0 <= c < N

def find_bfs(r, c, passenger):
  visited = [[False] * N for _ in range(N)]
  candidate = []
  q = deque()
  q.append((r, c, 0))
  min_distance = 1000000
  
  while q:
    c_r, c_c, distance = q.popleft()
    if distance > min_distance: # 더 먼 거리에 있는 승객은 태우지 X
      break
    if (c_r, c_c) in passenger: # 키들만 따로 안 모아도 되네?
      candidate.append((c_r, c_c)) # 같은 맨해튼 거리일 때, 정렬해주기 위해서
      min_distance = distance
    
    for i in range(4):
      n_r = c_r + dr[i]
      n_c = c_c + dc[i]
      if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
        if maps[n_r][n_c] == 0:
          q.append((n_r, n_c, distance+1))
          visited[n_r][n_c] = True
  return candidate, min_distance

def depart_bfs(r, c, pdr, pdc):
  visited = [[False] * N for _ in range(N)]
  used_fuel = 0
  q = deque()
  q.append((r, c, used_fuel))

  while q:
    c_r, c_c, used_fuel = q.popleft()
    if c_r == pdr and c_c == pdc:
      return used_fuel

    for i in range(4):
      n_r = c_r + dr[i]
      n_c = c_c + dc[i]
      if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
        if maps[n_r][n_c] == 0:
          q.append((n_r, n_c, used_fuel+1))
          visited[n_r][n_c] = True
  return 10000000

q = deque()
q.append((t_r, t_c))
# 연료가 다 떨어지거나 더 태울 승객이 없을 때까지
while fuel > 0 or len(passenger) != 0:
  # 현재 택시 기준으로 가장 가까운 사람 찾기
  s_r, s_c = q.popleft()
  candidate, used_fuel = find_bfs(s_r, s_c, passenger)
  fuel -= used_fuel
  if fuel < 0 or len(candidate) == 0:
    answer = -1
    break
  pr, pc = sorted(candidate)[0] # 맨해튼 거리가 같으면, 행&열 순으로 정렬
  pdr, pdc = passenger[(pr, pc)]
  del passenger[(pr, pc)]
  
  # 가까운 사람을 바탕으로 목적지까지 가기
  used_fuel = depart_bfs(pr, pc, pdr, pdc)
  fuel -= used_fuel
  if fuel < 0:
    answer = -1
    break
  fuel += used_fuel * 2
  if len(passenger) == 0:
    answer = fuel
    break
  q.append((pdr, pdc))

if answer == -1:
  print(-1)
else:
  print(answer)