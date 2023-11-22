N, L = map(int, input().split())
waters = []
for _ in range(N):
  start, end = map(int, input().split())
  waters.append((start, end))

waters.sort()
cnt, cur = 0, 0

for start, end in waters:
  if start > end:
    continue
  if cur > start:
    start = cur
  while start < end:
    start += L
    cnt += 1
  cur = start

print(cnt)