import sys
input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
  s = input().split()
  if s[0] == 'push':
    stack.append(s[1])
    
  elif s[0] == 'pop':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
      
  elif s[0] == 'size':
    print(len(stack))
    
  elif s[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
      
  elif s[0] == 'top':
    if len(stack) > 0:
      print(stack[-1])
    else:
      print(-1)
