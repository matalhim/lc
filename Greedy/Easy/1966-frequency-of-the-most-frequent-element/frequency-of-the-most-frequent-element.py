class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = summ = res = 0
        nums.sort()
        for r in range(len(nums)):
            summ += nums[r]
            while nums[r] * (r - l + 1) - summ > k:
                summ -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
            
        