class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)

        for i in range(n + 1):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < i:
                    l = m + 1
                else:
                    r = m - 1
            if n - l == i:
                return i
        
        return -1