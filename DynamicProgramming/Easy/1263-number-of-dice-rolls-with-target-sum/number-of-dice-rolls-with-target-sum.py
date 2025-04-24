class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7
        
        for _ in range(n):
            for i in range(target, -1, -1):
                dp[i] = 0
                for score in range(1, k + 1):
                    if i >= score:
                        dp[i] = (dp[i] + dp[i - score]) % mod
        return dp[target]
