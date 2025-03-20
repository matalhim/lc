class Solution:
    def largestInteger(self, num: int) -> int:
        digits: list = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        digits = digits[::-1]
        
        odd, even = [], []
        for d in digits:
            if d % 2 == 0:
                even.append(d)
            else:
                odd.append(d)
        odd.sort()
        even.sort()
        res = 0
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res
        