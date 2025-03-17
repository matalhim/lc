class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenate: list[int] = [int(x) for x in str(n) + str(2 * n) + str(3 * n)]
        nums_set: set[int] = set([x for x in range(1, 10)])
        
        return nums_set == set(concatenate) and len(concatenate) == len(nums_set)

        