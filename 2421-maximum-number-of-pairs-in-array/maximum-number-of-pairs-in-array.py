class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq: dict = {}
        res: list = [0] * 2

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for value in freq.values():
            res[0] += value // 2
            res[1] += value % 2
        
        return res
        

        