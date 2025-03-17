class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq: dict[str: int] = {}
        summ: int = 0
        for char in stones:
                freq[char] = freq.get(char, 0) + 1

        for char in jewels:
            summ += freq.get(char, 0)
 
        return summ