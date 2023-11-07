N = int(input())
cows = []
for _ in range(N):
  end, ch = map(int, input().split())
  cows.append((end, ch))

cows.sort()
t = 0

for cow in cows:
  end, ch = cow
  if t >= end:
    t += ch
  elif t < end:
    t = end + ch

print(t)