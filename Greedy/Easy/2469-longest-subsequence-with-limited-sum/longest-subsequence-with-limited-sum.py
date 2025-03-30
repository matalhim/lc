class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res: list[int] = []
        p: list[int] = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            p[i+1] = p[i] + nums[i]
        
        for summ in queries:
            l, r = 0, len(nums)
            while l <= r:
                m = l + (r - l) // 2
                if p[m] <= summ:
                    l = m + 1
                else:
                    r = m - 1
            res.append(r)
        
        return res
        