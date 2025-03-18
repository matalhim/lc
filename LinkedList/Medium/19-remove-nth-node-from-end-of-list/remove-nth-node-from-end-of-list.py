# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumpy = ListNode()
        dumpy.next = head
        right = head
        left = dumpy

        for _ in range(n):
            if right:
                right = right.next
            else: return head
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dumpy.next