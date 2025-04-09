class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        summ: int = sum(nums)
        curr_summ: int = 0
        res: list[int] = []
        for n in nums:
            curr_summ += n
            res.append(n)
            if curr_summ > summ - curr_summ:
                break
        return res