class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hash = [[i, val] for i, val in enumerate(nums)]
        sort_hash = sorted(hash, key=lambda x: x[1], reverse=True)
        res = [n[1] for n in sorted(sort_hash[:k], key = lambda x: x[0])]
        return res


        