class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_p = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+1] > nums[i+2]:
                max_p = nums[i] + nums[i+1] + nums[i+2]
        return max_p
