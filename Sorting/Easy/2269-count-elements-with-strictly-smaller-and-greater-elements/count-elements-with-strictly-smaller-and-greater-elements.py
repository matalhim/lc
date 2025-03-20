class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = 0
        nums.sort()
        for i in range(1, len(nums)-1):
            prev_c = c
            if nums[i] == nums[0]:
                c += 1
            if nums[len(nums) - 1 - i] == nums[len(nums) - 1]:
                c += 1
            if prev_c == c:
                break
        
        return 0 if len(nums) - 2 - c < 0 else len(nums) - 2 - c

                


        