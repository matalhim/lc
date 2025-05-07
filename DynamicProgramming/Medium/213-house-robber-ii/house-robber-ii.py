class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            l, r = 0, 0
            for n in nums:
                l, r = r, max(r, l + n)
            return r
        
        if len(nums) == 1:
            return nums[0]
        return max(rob(nums[:-1]), rob(nums[1:]))