# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 1->2->3->4
        # 4->5->6
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr = nxt
        first = head
        second = prev
        while second and second.next:
            tmp = first.next
            first.next=second
            first=tmp

            tmp = second.next
            second.next = first
            second =tmp
