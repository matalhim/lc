class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = cost[0]
        for i in range(2, len(cost) + 1):
            dp[i] = cost[i-1] + min(dp[i-1], dp[i-2])
        return min(dp[len(cost)], dp[len(cost)-1])