class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = res = nums[0]
        if len(nums) == 1:
            return res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mn, mx = mx, mn
            mn = min(nums[i], mn * nums[i])
            mx = max(nums[i], mx * nums[i])
            res = max(res, mx)
        return res


        