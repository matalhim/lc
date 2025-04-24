class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort() # (w,l,h)
        cuboids.sort()
        n = len(cuboids)
        dp = [cub[2] for cub in cuboids]
        for i in range(n):
            h = cuboids[i][2]
            for j in range(i):
                if (
                    cuboids[i][0] - cuboids[j][0] >= 0 and 
                    cuboids[i][1] - cuboids[j][1] >= 0 and 
                    h - cuboids[j][2] >= 0):
                    dp[i] = max(dp[i], dp[j] + h)
        return max(dp)