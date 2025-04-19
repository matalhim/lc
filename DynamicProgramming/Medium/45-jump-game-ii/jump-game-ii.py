class Solution:
    def jump(self, nums: List[int]) -> int:
         dp=[len(nums)] * len(nums)
         if len(nums)==1:
            return 0
         dp[0], dp[1] = 0, 1
         for i in range(2, len(nums)):
             for j in range(i):
                if i-j <= nums[j]:
                    dp[i] = min(dp[i], dp[j]+1) 
         return dp[-1]

