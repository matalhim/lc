class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_len = len(grid[0])
        res = 0
        r_max = row_len
        for row in grid:
            l, r = 0, r_max - 1
            while l <= r:
                m = l + (r - l) // 2
                if row[m] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            res += (row_len - l)
            r_max = r + 1

        return res

        