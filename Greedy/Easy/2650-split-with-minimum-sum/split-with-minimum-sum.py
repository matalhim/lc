class Solution:
    def splitNum(self, num: int) -> int:
        digits: list[int] = []

        while num > 0:
            digits.append(num % 10)
            num = num // 10
        
        res = i = 0
        k: int = 1
        digits = sorted(digits, reverse=True)

        while i < len(digits) - 1:
            res += (digits[i] + digits[i + 1]) * k
            k *= 10
            i += 2
        

        return res if len(digits) % 2 == 0 else res + digits[-1] * k





        