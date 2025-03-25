class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res: list[int] = []

        starts = [[interval[0], i] for i, interval in enumerate(intervals)]
        starts = sorted(starts, key=lambda x: x[0])
        
        for interval_i in intervals:
            end_i = interval_i[1]
            j = -1 
            l, r = 0, len(starts) - 1
            while l <= r:
                m = l + (r - l) // 2
                if starts[m][0] >= end_i:
                    r = m - 1
                    j = starts[m][1]
                else:
                    l = m + 1
            res.append(j)
        
        return res
            
            
        