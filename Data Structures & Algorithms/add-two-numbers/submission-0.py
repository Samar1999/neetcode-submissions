# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = result = ListNode()
        carry = 0

        while l1 or l2:
            
            res = 0 + carry

            if l1:
                res += l1.val
                l1 = l1.next
            
            if l2:
                res += l2.val
                l2 = l2.next

            carry = res//10
            res = res % 10
            result.next = ListNode(res)
            result = result.next
        
        if carry==1:
            result.next = ListNode(carry)

        return p1.next



