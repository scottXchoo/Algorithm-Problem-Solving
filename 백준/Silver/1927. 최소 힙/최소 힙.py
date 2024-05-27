from heapq import heappush, heappop

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

ans = []
for num in nums:
    if num == 0:
        if len(ans) == 0:
            print(0)
        else:
            print(heappop(ans))
    else:
        heappush(ans, num)