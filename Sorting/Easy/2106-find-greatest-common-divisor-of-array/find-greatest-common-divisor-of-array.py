class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        nums.sort()
        return gcd(nums[0], nums[-1])
        