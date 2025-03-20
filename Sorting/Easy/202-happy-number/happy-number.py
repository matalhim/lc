def square(n: int) -> int:
    summ = 0
    while n > 0:
        d = n % 10 
        summ += d ** 2 
        n = n // 10     
    return summ


class Solution:
    def isHappy(self, n: int) -> bool:
        freq: dict[int, int] = {}

        while n != 1:
            n = square(n)
            if n in freq:
                return False
            freq[n] = 1
        
        return True





        