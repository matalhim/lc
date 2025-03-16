class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq: dict = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1
        
        for char in s:
            if char in s:
                freq[char] -= 1
            else:
                return char
        
        return next((key for key, value in freq.items() if value == 1))
        