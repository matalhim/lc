class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a, b = sum(aliceSizes), sum(bobSizes)
        alice_set = set(aliceSizes)
        for b_give in bobSizes:
            a_give = (a - b + 2 * b_give) // 2
            if a_give in alice_set:
                return [a_give, b_give]


        