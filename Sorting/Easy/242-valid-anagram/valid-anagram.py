class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s: dict[str, int] = {}
        freq_t: dict[str, int] = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        return freq_s == freq_t

        