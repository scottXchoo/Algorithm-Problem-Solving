class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2      
        ans = abs(sum(nums[:N]) - sum(nums[N:]))
        total = sum(nums) 
        half = total // 2 
        
        for k in range(1, N):
            left = [sum(comb) for comb in combinations(nums[:N], k)]
            right = [sum(comb) for comb in combinations(nums[N:], N-k)]
            right.sort()
            for x in left:
                r = half - x # ?!?!? half
								# ?! 합 차이 최소가 되려면, 두 개를 더했을 때, 절반 값이 되어야 한다.
								## 꼭 절반이어야할까?! 모든 경우에서 절반일까?! + '부분의 합'
                p = bisect.bisect_left(right, r) 
                if 0 <= p < len(right):
                    left_ans_sum = x + right[p]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(left_ans_sum - right_ans_sum)
                    ans = min(ans, diff)
        return ans