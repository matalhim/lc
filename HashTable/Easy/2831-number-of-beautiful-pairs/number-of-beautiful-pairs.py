class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        def first_digit(n: int) -> int:
            while n >= 10:
                n //= 10
            return n

        res: int = 0
        first_freq = [0] * 10 
        
        for n in nums:
            last = n % 10 
            for first in range(10):
                if first_freq[first] > 0 and gcd(first, last) == 1:
                    res += first_freq[first]
            first = first_digit(n)
            first_freq[first] += 1
        
        return res