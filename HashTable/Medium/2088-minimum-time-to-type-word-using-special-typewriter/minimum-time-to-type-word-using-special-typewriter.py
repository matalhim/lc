class Solution:
    def minTimeToType(self, word: str) -> int:
        a_z: int = ord('z') - ord('a') + 1
        prev: int = ord('a')
        res: int = 0
        for char in word:
            curr = ord(char)
            if curr != prev:
                d = abs(curr - prev)
                res += min(d, a_z - d)
            res += 1
            prev = curr
        
        return res






        