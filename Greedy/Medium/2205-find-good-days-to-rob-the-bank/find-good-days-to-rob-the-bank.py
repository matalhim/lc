class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n: int = len(security)
        if time == 0:
            return list(range(n))
        if n < 2 * time + 1:
            return []
        
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            if security[i-1] >= security[i]:
                l[i] = l[i-1] + 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                r[i] = r[i+1] + 1
        res: list[int] = []
        for i in range(time, n - time):
            if l[i] >= time + 1 and r[i] >= time + 1:
                res.append(i)
        return res

        

        