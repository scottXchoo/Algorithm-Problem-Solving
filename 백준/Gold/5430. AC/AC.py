from collections import deque
T = int(input())

for _ in range(T):
  F = input()
  N = int(input())
  arr = input()[1:-1].split(',')

  dq = deque(arr)
  flag = 0

  if N == 0:
    dq = deque([])

  for i in F:
    if i == 'R':
      flag += 1
    elif i == 'D':
      if len(dq) == 0:
        print("error")
        break
      else:
        if flag % 2 == 0:
          dq.popleft()
        else:
          dq.pop()

  else:
    if flag % 2 == 0:
      print("[" + ",".join(dq) + "]")
    else:
      dq.reverse()
      print("[" + ",".join(dq) + "]")
