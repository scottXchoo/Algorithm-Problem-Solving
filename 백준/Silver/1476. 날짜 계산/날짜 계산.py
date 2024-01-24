import sys
from itertools import cycle

E, S, M = map(int, input().split())

arr = [
    cycle(list(range(1, 16))),
    cycle(list(range(1, 29))),
    cycle(list(range(1, 20)))
]

year = 1
while True:
  e_y = next(arr[0])
  s_y = next(arr[1])
  m_y = next(arr[2])
  if e_y == E and s_y == S and m_y == M:
    print(year)
    break
  else:
    year += 1