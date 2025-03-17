class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # обход дерева inorder
        def inorder(node, nums):
            if node:
                inorder(node.left, nums)
                nums.append(node.val)
                inorder(node.right, nums)
        
        nums: list[int] = []
        inorder(root, nums)

        # получаю отсортированный список значений и использую два указателя
        l: int
        r: int
        l, r = 0, len(nums) - 1
        while l < r:
            summ = nums[l] + nums[r]
            if summ == k:
                return True
            elif summ < k: l += 1
            else:  r -= 1
        
        return False
        