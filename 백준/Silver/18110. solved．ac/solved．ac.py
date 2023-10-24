import math

N = int(input())
pb = [int(input()) for _ in range(N)]
pb.sort()
arr = []

def rounded(value):
  integer = math.floor(value)
  if value - integer == 0:
    return int(value)
  elif value - integer < 0.5:
    return int(integer)
  else:
    return int(integer + 1)

k = rounded(N * 0.15)
for i in range(k, N - k):
  arr.append(pb[i])

if len(arr) == 0:
  print(0)
else:
  ans = sum(arr) / len(arr)
  print(rounded(ans))