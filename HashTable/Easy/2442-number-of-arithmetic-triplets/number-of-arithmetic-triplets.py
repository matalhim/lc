class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = 0
        for num in nums:
            if (num - diff) in nums and (num + diff) in nums:
                c += 1      
        return c