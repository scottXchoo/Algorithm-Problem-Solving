T = int(input())

for _ in range(T):
  A = list(map(str, input().split()))
  answer = 0
  for i in range(len(A)):
    if i == 0:
      answer += float(A[i])
    else:
      if A[i] == "#":
        answer -= 7
      elif A[i] == "%":
        answer += 5
      elif A[i] == "@":
        answer *= 3
  print("%0.2f" % answer)