class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m: int = len(students)
        n: int = len(students[0])
        scores: list[list[int]] = [[0] * m for _ in range(m)]
        
        def count_score(a: list[int], b: list[int]) -> int: 
            return sum([x == y for x, y in zip(a, b)])
        
        for i in range(m):
            for j in range(m):
                scores[i][j] = count_score(students[i], mentors[j])
        
        dp = [-1] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):
            if dp[mask] == -1:
                continue
            j = bin(mask).count('1')
            for i in range(m):
                if not mask & (1 << i):
                    next = mask | 1 << i
                    dp[next] = max(dp[next], dp[mask] + scores[j][i])
        return dp[-1]