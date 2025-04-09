class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res: int = 0
        for i in range(0, len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff <= 0 :
                res += abs(diff) + 1
                nums[i+1] = nums[i] + 1
        return res

        