class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq: dict[int: int] = {}
        left: dict[int: int] = {}
        right: dict[int: int] = {}

        l: int = len(nums)
        if l == 1: return 1

        for i in range(l):
            if nums[i] in freq:
                freq[nums[i]] += 1
                right[nums[i]] = i
            else:
                freq[nums[i]] = 1
                left[nums[i]] = i
        degree = max(freq.values())
        
        if degree == 1:
            return 1
        
        for n in freq:
            if freq[n] == degree:
                l = min(l, right[n] - left[n] + 1)
        
        return l

        