class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                res.append(mid)
                i = mid - 1
                while i >= 0 and nums[i] == target:
                    res.append(i)
                    i -= 1
                i = mid + 1
                while i < len(nums) and nums[i] == target:
                    res.append(i)
                    i += 1
                res.sort()
                return res

        return res