class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len: int = 1
        freq: dict = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        summ = 0
        odd = 0
        
        for c in freq.values():
            if c % 2 == 0:
                summ += c
            else:
                summ += c - 1  
                odd += 1
        
        if odd > 0:
            summ += 1
        
        return summ
        