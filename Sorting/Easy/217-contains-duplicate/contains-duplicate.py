class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq: dict[int: int] = {}
        for n in nums:
            if n in freq:
                return True
                freq[n] += 1
            else:
                freq[n] = 1
            
        return False