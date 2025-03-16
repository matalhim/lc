class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq: dict[int: int] = {}
        for n in nums:
            if n %2 == 0:
                freq[n] = freq.get(n, 0) + 1
        
        if not freq:
            return -1

        max_freq = max(freq.values())
        return min([num for num, count in freq.items() if count == max_freq])
        