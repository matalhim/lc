class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ: int = sum(nums)
        if summ % 2 != 0:
            return False
        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(len(dp) - n - 1, -1, -1):
                if dp[i]:
                    dp[i+n] = True
        return dp[target]
                
        
        
        