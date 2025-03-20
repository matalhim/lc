class Solution:
    def isThree(self, n: int) -> bool:
        freq: dict[int, int] = {}
        i: int = 2
        res: int = 1
        while i*i <= n:
            while n % i == 0:
                freq[i] = freq.get(i, 0) + 1
                n = n // i
            i += 1
        if n > 1:
            freq[n] = 1

        for val in freq.values():
            res *= (val + 1)
        return res == 3


        