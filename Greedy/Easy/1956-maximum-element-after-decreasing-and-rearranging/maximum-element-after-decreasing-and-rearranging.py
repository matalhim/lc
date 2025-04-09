class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        l = 0
        arr.sort()
        for r in arr:
            if r > l:
                l += 1
        return l



        