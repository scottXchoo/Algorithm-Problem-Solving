N = int(input())
list = []

for _ in range(N):
  weight, height = map(int, input().split())
  list.append((weight, height))

for i in list:
  rank = 1
  for j in list:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  print(rank, end = " ")