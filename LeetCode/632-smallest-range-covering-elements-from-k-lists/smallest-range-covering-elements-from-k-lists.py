class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = sys.maxsize
        maxValue = -sys.maxsize
        left, right = 0, 0
        minHp, values = [], []
        for k_idx, num in enumerate(nums):
            values.append(num[0])
            maxValue = max(maxValue, num[0])
            heapq.heappush(minHp, (num[0], 0, k_idx))

        while True:
            minValue, minIdx, minK = heapq.heappop(minHp)
            if ans > maxValue - minValue:
                left = minValue
                right = maxValue
                ans = maxValue - minValue

            if len(nums[minK]) > minIdx+1:
                n_num = nums[minK][minIdx+1]
                heapq.heappush(minHp, (n_num, minIdx+1, minK))
                maxValue = max(maxValue, n_num)
            else:
                break

        return [left, right]