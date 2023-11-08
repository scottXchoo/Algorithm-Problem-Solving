N = int(input())
arr = []
a = [False, False] + [True] * (N - 1)

for i in range(2, N + 1):
  if a[i]:
    arr.append(i)
    for j in range(2 * i, N + 1, i):
      a[j] = False

ans, start, end = 0, 0, 0
while end <= len(arr):
  temp_sum = sum(arr[start:end])
  if temp_sum == N:
    ans += 1
    end += 1
  elif temp_sum < N:
    end += 1
  else:
    start += 1

print(ans)