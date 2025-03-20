class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = [1, 2]
        if n < 3:
            return n
        for _ in range(2, n):
            num_ways.append(num_ways[-1] + num_ways[-2])
        return num_ways[-1]