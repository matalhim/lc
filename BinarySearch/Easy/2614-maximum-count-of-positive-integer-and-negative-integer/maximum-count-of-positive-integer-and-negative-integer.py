class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m - 1
        
        lt, l, r = l, 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m - 1

        gt = len(nums) - l
        return max(lt, gt)
        


        