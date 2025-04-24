class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, stock = 0, -1e5
        for p in prices:
            prev = res
            res = max(res, stock + p)
            stock = max(stock, res - p)
        return res
