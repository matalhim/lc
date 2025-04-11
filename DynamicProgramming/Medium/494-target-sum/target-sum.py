class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p + n = sum, p - n = target
        # p = (sum + target) / 2
        summ: int = sum(nums)
        if (summ + target) % 2 != 0 or abs(target) > summ:
            return 0
        
        p = (summ + target) // 2
        dp = [0] * (p + 1)
        dp[0] = 1
        for n in nums:
            for i in range(p, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[p]
        