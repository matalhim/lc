class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        summ = sum(max(row) for row in mat)
        if target > summ:
            return target - summ

        dp = [-1] * (summ + 1)
        
        for n in mat[0]:
                dp[n] = 1

        for row in mat[1:]:
            new_dp = [-1] * (summ + 1)
            for i in range(summ + 1):
                if dp[i] == 1:
                    for n in row:
                        if i + n <= summ:
                            new_dp[i + n] = 1
            dp = new_dp
        
        diff = summ
        for i in range(summ + 1):
            if dp[i] == 1:
                curr_diff = abs(target - i)
                if curr_diff == 0: 
                    return 0
                if curr_diff < diff:
                    diff = curr_diff
        
        return diff
        