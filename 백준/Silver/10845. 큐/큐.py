import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque()

for _ in range(N):
  s = input().split()
  if s[0] == 'push':
    q.append(s[1])
    
  elif s[0] == 'pop':
    if len(q) > 0:
      print(q.popleft())
    else:
      print(-1)
      
  elif s[0] == 'size':
    print(len(q))
    
  elif s[0] == 'empty':
    if len(q) == 0:
      print(1)
    else:
      print(0)
      
  elif s[0] == 'front':
    if len(q) > 0:
      print(q[0])
    else:
      print(-1)
  
  elif s[0] == 'back':
    if len(q) > 0:
      print(q[-1])
    else:
      print(-1)
