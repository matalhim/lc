class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # p - n = w, p + n = summ
        # p = summ // 2
        summ = sum(stones)
        dp = [False] * (summ // 2 + 1)
        dp[0] = True

        for s in stones:
            for i in range(summ // 2, s - 1, -1):
                if dp[i-s]:
                    dp[i] = True
        p = max([i if dp[i] else 0 for i in range(summ // 2 + 1)])
        return summ - 2 * p
