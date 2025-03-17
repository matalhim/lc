class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res: set(int) = set()
        l: int = 0
        r: int = len(nums) - 1
        nums = sorted(nums)
        while r > l:
            average = (nums[l] + nums[r]) / 2
            res.add(average)
            l += 1
            r -= 1
        
        return len(res)


        