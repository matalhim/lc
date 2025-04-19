class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) + 1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            step = nums[i]
            for j in range(1, step + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[len(nums) - 1]

