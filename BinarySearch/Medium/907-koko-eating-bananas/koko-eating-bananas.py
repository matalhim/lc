class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2

            summ_h = 0
            for p in piles:
                summ_h += p // m + 1
                if p % m == 0:
                    summ_h -= 1
            
            if summ_h <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

        