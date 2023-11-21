from collections import deque

T = int(input())
# [0]을 맨 처음에 두면, 쉬워짐
## [0, deque([...]), deque([...]) ... deque([...])]
gears = [0] + [deque(map(int, list(input()))) for _ in range(T)] 
K = int(input())
turn = [list(map(int, input().split())) for _ in range(K)]

def solution(T, gears, K, turn):
  for t, direct in turn:
    turnElement = []
    # t 기준 오른쪽 기어
    for i in range(t+1, T+1):
      if gears[i][6] != gears[i-1][2]:
        turnElement.append(i)
      else:
        break
    # t 기준 왼쪽 기어
    for i in range(t-1, 0, -1):
      if gears[i][2] != gears[i+1][6]:
        turnElement.append(i)
      else:
        break
    # t 기어 회전
    gears[t].rotate(direct)
    # t 기어와 맞닿은 극이 다른 기어 회전
    for element in turnElement:
      gears[element].rotate(-direct if (element-t)%2 else direct)
  return sum(gears[i][0] for i in range(1, T+1))

ans = solution(T, gears, K, turn)
print(ans)