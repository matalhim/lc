class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        summ = sum(nums)
        dp = [0] * (n)
        dp[0] = sum(i * nums[i] for i in range(n))
        for i in range(1, n):
            dp[i] = summ - n * nums[n-i] + dp[i-1]
        return max(dp)