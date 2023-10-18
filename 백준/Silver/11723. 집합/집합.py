import sys
input = sys.stdin.readline
N = int(input())
s = set()

for _ in range(N):
  x = input().strip().split()

  if len(x) == 1:
    if x[0] == 'all':
      s = set([i for i in range(1, 21)])
    else:
      s = set()
    continue

  if x[0] == 'add':
    s.add(int(x[1]))

  elif x[0] == 'remove':
    s.discard(int(x[1]))

  elif x[0] == 'check':
    print(1 if int(x[1]) in s else 0)

  elif x[0] == 'toggle':
    if int(x[1]) in s:
      s.discard(int(x[1]))
    else:
      s.add(int(x[1]))