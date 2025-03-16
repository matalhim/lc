class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq: dict = {}
        for char in magazine:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in ransomNote:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        
        return all(value >= 0 for value in freq.values())


        