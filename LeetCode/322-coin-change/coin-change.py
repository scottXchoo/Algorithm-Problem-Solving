class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0

            retList = []
            for coin in coins:
                remain_amount = amount - coin
                if remain_amount >= 0:
                    if remain_amount not in memo:
                        memo[remain_amount] = dp(remain_amount)
                    if memo[remain_amount] != -1:
                        retList.append(memo[remain_amount])
            return min(retList) + 1 if retList else -1

        return dp(amount)