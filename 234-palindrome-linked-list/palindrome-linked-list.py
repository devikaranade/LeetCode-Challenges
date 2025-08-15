# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow 
        prev = None
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev=curr
            curr = nxt
        first = head
        second = prev
        while second:
            if first.val!=second.val:
                return False
            first = first.next
            second = second.next
        return True

        

        
