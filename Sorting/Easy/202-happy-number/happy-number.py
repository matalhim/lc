def square(num):
    return sum(n * n for n in num)

def to_digits(n):
    re: list[int] = []
    while n > 0:
        re.append(n %10)
        n = n // 10
    return re


class Solution:
    def isHappy(self, n: int) -> bool:
        freq: dict[int, int] = {}

        while n != 1:
            n = square(to_digits(n))
            if n in freq:
                return False
            freq[n] = 1
        
        return True





        