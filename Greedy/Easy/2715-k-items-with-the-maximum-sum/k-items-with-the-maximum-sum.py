class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        one = min(numOnes, k)
        res += one
        rem = k - one
        
        if rem <= 0:
            return res
        
        zero = min(numZeros, rem)
        rem -= zero
        
        if rem <= 0:
            return res
        
        return res - rem