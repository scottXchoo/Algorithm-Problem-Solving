N = int(input())
ans = 0

for i in range(1, N+1):
  nums = list(map(int, str(i)))
  ans = sum(nums) + i
  if ans == N:
    print(i)
    break
  if i == N:
    print(0)