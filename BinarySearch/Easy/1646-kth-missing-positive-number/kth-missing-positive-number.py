class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # miss count = arr[i] - (i+1)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            miss_count = arr[m] - m - 1
            if miss_count < k:
                l = m + 1
            else:
                r = m - 1
            
        return l + k

 

        