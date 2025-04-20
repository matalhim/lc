class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [200 * m * n] * n
        dp[0] = 0 

        for row in grid:
            dp[0] += row[0] 
            for j in range(1, n):
                dp[j] = row[j] + min(dp[j], dp[j - 1])

        return dp[-1]
        