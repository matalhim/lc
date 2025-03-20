class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res: int = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                if (num2 & (num2 - 1)) == 0:
                    res += num1 // num2
                    num1 &= (num2 - 1)
                else:
                    res += num1 // num2
                    num1 %= num2
            else:
                if (num1 & (num1 - 1)) == 0:
                    res += num2 // num1
                    num2 &= (num1 - 1)
                else:
                    res += num2 // num1
                    num2 %= num1
        return res