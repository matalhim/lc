class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set: set[str] = set(jewels)
        freq: dict[str: int] = {}
        for char in stones:
            if char in jewels_set:
                freq[char] = freq.get(char, 0) + 1
        
        return sum(freq.values())