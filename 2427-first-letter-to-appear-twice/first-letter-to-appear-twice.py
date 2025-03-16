class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq: dict = {}
        for char in s:
            if char in freq:
                return char
            else:
                freq[char] = 1
        