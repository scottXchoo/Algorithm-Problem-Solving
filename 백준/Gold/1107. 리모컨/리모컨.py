import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))

min_cnt = abs(100 - N)  # [1] 현재 채널에서 +/-만 사용해서 이동

for nums in range(1000001):  # [2] 무식하게 0부터 1000000까지
  nums = str(nums)

  for j in range(len(nums)):
    if int(nums[j]) in broken:  # [3] nums에 broken가 있다면, break
      break
      
    elif j == len(nums) - 1:  # [4] 마지막까지 왔다면, min_cnt 비교 후 업데이트
      min_cnt = min(min_cnt, abs(int(nums) - N) + len(nums))

print(min_cnt)