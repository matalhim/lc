class Solution:
    def trap(self, height: List[int]) -> int:        
        n = len(height)
        l: list[int] = [0] * n
        r: list[int] = [0] * n
        w: int = 0
        l[0] = height[0]
        for i in range(1, n):
            l[i] = max(l[i-1], height[i])
        
        r[-1] = height[-1]
        for i in range(n-2, -1, -1):
            r[i] = max(r[i+1], height[i])

        for i in range(n):
            w += min(l[i], r[i]) - height[i]
        return w