class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_i, num_j = 0, 0
        for num in nums:
            if num > num_i:
                num_i, num_j = num, num_i
            elif num > num_j:
                num_j = num
        return (num_i - 1) * (num_j - 1)
        