class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] + [0] * (n - 1) for _ in range(m)]
        dp[0] = [1] * n
        for j in range(1, m):
            for i in range(1, n):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m-1][n-1]
        