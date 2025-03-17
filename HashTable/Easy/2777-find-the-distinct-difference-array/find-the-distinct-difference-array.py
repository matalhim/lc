class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # prefix nums[0,...,i]
        # suffix nums[i+1,...,n-1]
        pref: list[int] = []
        suff: list[int] = [0] * len(nums)
        res: list[int] = []

        nums_set: set[int] = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])
            pref.append(len(nums_set))
        
        nums_set = set()
        for i in range(len(nums) - 1, -1, -1):
            suff[i] = len(nums_set)
            nums_set.add(nums[i])

        for i in range(len(nums)):
            res.append(pref[i] - suff[i])
        
        return res




        