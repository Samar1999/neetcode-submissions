# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        l = 0

        while curr:
            curr = curr.next
            l +=1

        if n == l:
            return head.next

        p = 0
        p1 = head
        while p1:
            if p == l - n - 1:
                p1.next = p1.next.next
                return head
            p += 1
            p1 = p1.next
        
