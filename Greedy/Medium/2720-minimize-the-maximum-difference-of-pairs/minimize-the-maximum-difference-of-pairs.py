class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        def is_p_pairs(diff):
            c = i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= diff:
                    c += 1
                    i += 2
                else:
                    i += 1
                if c == p:
                    return True
            return False
            
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            if is_p_pairs(m):
                r = m
            else:
                l = m + 1
        return l
        