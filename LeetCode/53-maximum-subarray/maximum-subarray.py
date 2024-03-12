class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if dp[i-1] + nums[i] <= nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)