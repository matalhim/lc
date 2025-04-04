# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l = None
        while slow:
            temp = slow.next
            slow.next = l
            l = slow
            slow = temp
        
        tail = l
        while tail:
            if tail.val == head.val:
                tail = tail.next
                head = head.next
            else:
                return False
        
        return True

        