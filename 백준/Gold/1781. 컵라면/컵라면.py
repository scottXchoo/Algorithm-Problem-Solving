from heapq import heappop, heappush

N = int(input())
pbs = []
for _ in range(N):
  dl, num = map(int, input().split())
  pbs.append((dl, num))

pbs.sort()
q = []

for pb in pbs:
  dl, num = pb
  heappush(q, num)
  if len(q) > dl:
    heappop(q)

print(sum(q))