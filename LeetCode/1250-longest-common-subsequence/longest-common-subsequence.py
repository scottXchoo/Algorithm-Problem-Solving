class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[n][m]
        