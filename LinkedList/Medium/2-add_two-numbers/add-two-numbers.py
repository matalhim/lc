# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        add = 0

        while l1 or l2:
            a = b = 0

            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + add
            add = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

        if add:
            cur.next = ListNode(add)

        return dummy.next