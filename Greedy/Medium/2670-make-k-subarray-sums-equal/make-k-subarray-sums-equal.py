class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        def gcd(a, b):
            while a > 0 and b > 0:
                if a >= b:
                    a = a % b
                else:
                    b = b % a
            return max(a, b)
        
        g = gcd(len(arr), k)
        res: int = 0

        for gi in range(g):
            nums = []
            for i in range(gi, len(arr), g):
                nums.append(arr[i])
            
            nums.sort()
            m = nums[len(nums) // 2]
            res += sum(abs(n - m) for n in nums)
        
        return res
