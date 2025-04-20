class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[200 * m * n] + [0] * (n) for _ in range(m+1)]
        dp[0] = [200 * m * n] * (n+1)
        dp[1][0] = 0
        print(dp)
        for j in range(1, m+1):
            for i in range(1, n+1):
                dp[j][i] = grid[j-1][i-1] + min(dp[j-1][i], dp[j][i-1])
        print(dp)
        return dp[m][n]
        