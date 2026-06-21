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

        p1 = head
        for i in range(l - 1):
            if i == l - n - 1:
                p1.next = p1.next.next
                return head
            p1 = p1.next
        
