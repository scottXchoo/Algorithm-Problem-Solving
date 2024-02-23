class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i+coin] = min(dp[i+coin], dp[i]+1)

        return -1 if dp[amount] == sys.maxsize else dp[amount]