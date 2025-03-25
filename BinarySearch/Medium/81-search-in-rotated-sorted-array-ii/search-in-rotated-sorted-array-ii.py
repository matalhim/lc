class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            while l < m and nums[l] == nums[m]:
                l += 1
            while r > m and nums[r] == nums[m]:
                r -= 1
            
            if nums[m] >= nums[l]:
                # sorted слева
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # sorted справа
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return False
        