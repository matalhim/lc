class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        res: int = nums[0]

        while l <= r:
            res = min(res, nums[l])
            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # sorted слева
                l = m + 1
            else:
                # sorted справа
                r = m - 1
    
        return res
        