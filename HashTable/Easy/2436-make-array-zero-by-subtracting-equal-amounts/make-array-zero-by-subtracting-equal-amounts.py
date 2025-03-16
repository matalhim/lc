class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set: set = set(nums)
        return len([num for num in nums_set if num != 0])
        