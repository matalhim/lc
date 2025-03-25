class Solution:
    def arrangeCoins(self, n: int) -> int:
        l: int = 1
        r: int = n
        res: int = 1
        
        while l <= r:
            m = l + (r - l) // 2
            summ_m = m * (1 + m) // 2
            if summ_m <= n:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res

            
        