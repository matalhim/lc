# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = r = head
        for _ in range(k-1):
            r = r.next
        beg_k = r

        while r and r.next:
            r = r.next
            l = l.next
        
        beg_k.val, l.val = l.val, beg_k.val
        return head

        



