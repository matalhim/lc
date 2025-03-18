# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

        