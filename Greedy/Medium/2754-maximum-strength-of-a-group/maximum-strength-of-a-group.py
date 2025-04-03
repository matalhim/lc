class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        neg = [n for n in nums if n < 0]
        pos = [n for n in nums if n > 0]
        zeros = [n for n in nums if n == 0]
        
        if len(neg) % 2 != 0:
            neg.pop()
        
        not_zeros = neg + pos
        
        if not not_zeros:
            return 0 if zeros else nums[-1]
        
        res: int = 1
        for num in not_zeros:
            res *= num
        
        return res