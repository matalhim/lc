class Solution:
    def longestString(self, x: int, y: int, z: int) -> int: 
        m = min(x, y)
        a = x - m
        b = y - m
        res = m * 4 
        
        if a > 0:
            res += 2
        elif b > 0:
            res += 2

        res += z * 2
        return res
        