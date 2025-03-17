class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq: dict = {}
        for num in nums:
            for n in num:
                if n in freq:
                    freq[n] += 1
                else:
                    freq[n] = 1
            
        res: list = [n for n, c in freq.items() if c == len(nums)]
        return sorted(res)