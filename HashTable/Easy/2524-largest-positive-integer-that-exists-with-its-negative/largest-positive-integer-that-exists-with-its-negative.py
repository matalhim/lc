class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set: set[int] = set(nums)
        res = -1
        for n in nums:
            if n > 0 and -n in nums_set:
                res = max(res, n)

        return res