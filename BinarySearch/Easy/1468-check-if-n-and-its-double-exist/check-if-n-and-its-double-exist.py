class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)):

            target = 2 * arr[i]
            l, r = 0, len(arr) - 1
            j = len(arr)
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] > target:
                    r = m - 1
                elif arr[m] < target:
                    l = m + 1
                else:
                    if m != i:
                        return True
                    else:
                        break
        
        return False
            