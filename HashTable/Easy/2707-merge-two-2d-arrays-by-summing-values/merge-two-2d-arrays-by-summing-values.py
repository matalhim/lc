class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums: dict[int: int] = {}
        for i, n in nums1:
            nums[i] = nums.get(i, 0) + n
        for i, n in nums2:
            nums[i] = nums.get(i, 0) + n
            
        return sorted(nums.items(), key=lambda x: x[0])

        
        