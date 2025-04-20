class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m+1)]
        dp[1][0] = 1

        for j in range(1, m+1):
            for i in range(1, n+1):
                if obstacleGrid[j-1][i-1] != 1:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
        print(dp)
        return dp[m][n]
