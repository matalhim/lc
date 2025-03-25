class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            m_val = nums[m]

            if m_val == target:
                return m
            
            if nums[l] <= m_val:
                #sorted слева
                if target > m_val or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1    
            else:
                #sorted справа
                if target < m_val or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1