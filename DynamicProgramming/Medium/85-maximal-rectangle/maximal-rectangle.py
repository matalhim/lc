class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [0] * (m + 1)
        res = 0
        for r in matrix:
            for i in range(m):
                dp[i] = dp[i] + 1 if r[i] == '1' else 0
            s = [-1]
            for i in range(m + 1):
                while dp[i] < dp[s[-1]]:
                    x = dp[s.pop()]
                    y = i - s[-1] - 1
                    res = max(res, x * y)
                s.append(i)
        return res
            