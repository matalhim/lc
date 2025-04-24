class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (37 + 1)
        dp[0], dp[1], dp[2] = 0, 1 , 1
        if n < 2:
            return dp[n]
        for i in range(3, n + 1, 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        