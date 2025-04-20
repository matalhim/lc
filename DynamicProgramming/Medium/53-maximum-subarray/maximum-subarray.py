class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = res = nums[0]
        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            res = max(c, res)
        return res
