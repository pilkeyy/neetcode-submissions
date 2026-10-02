# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr1 = head
        curr2 = prev
        while curr1.next and curr2.next:
            tmp1= curr1.next
            tmp2 = curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1 = tmp1
            curr2 = tmp2