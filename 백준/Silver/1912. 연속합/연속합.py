N = int(input())
nums = list(map(int, input().split(' ')))

for i in range(1, N):
    nums[i] = max(nums[i], nums[i-1] + nums[i])

print(max(nums))