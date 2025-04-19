class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n+1] * n
        dp[0] = 0
        res = 0
        for i in range(n):
            if i > res:
                break
            step = nums[i]
            for j in range(1, step + 1):
                if i + j < n:
                    if dp[i + j] > dp[i] + 1:
                        dp[i + j] = dp[i] + 1
                        if i + j > res:
                            res = i + j
        return dp[n - 1]

