class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        res: int = 0
        l, r = 0 , 1
        while r < len(nums):
            if nums[l] < nums[r]:
                res += 1
                l += 1
            r += 1
        return res

