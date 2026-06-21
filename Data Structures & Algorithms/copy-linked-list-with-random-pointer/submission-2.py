# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return head

        curr = head
        while curr:
            newnode = Node(curr.val)
            newnode.next = curr.next
            curr.next = newnode
            curr = curr.next.next
        
        curr = head
        while curr:
            if curr.random: # Important check
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        p1 = head
        newhead = head.next

        while p1:
            p2 = p1.next
            p1.next = p2.next
            p1 = p1.next
            if p1:
                p2.next = p1.next

        return newhead
        