class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n: int = len(colors)
        res: int = 0

        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
                break
                
        for i in range(n):
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
                break
                
        return res
                
        
