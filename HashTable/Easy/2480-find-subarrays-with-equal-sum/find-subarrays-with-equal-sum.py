class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        summ: dict[int: int] = {}
        for i in range(1, len(nums)):
            summ[i-1] = nums[i-1] + nums[i]
        
        return len(set(summ.values())) < len(summ.values())

        