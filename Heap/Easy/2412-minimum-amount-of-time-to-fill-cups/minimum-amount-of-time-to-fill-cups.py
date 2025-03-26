class Solution:
    def fillCups(self, amount: List[int]) -> int:
        m = max(amount)
        t = sum(amount)
        return m if m > t - m else (t + 1) // 2
        
        