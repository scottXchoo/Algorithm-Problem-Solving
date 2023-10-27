M = int(input())
N = int(input())
sosu_list = []

for num in range(M, N+1):
  error = 0
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        error += 1
        break
    if error == 0:
      sosu_list.append(num)

if len(sosu_list) > 0:
  print(sum(sosu_list))
  print(min(sosu_list))
else:
  print(-1)