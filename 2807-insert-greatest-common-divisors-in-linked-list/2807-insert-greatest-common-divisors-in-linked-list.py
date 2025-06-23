# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def greatestCommonDivisors(self, n1, n2):
        """Euclidean Algorithm."""
        while n2 != 0:
            n1, n2 = n2, n1 % n2
        return abs(n1) 

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p1 = head
        p2 = head.next

        while p2:
            new_node = ListNode(self.greatestCommonDivisors(min(p1.val, p2.val), max(p1.val, p2.val)))
            p1.next = new_node
            new_node.next = p2
            p1 = p2
            p2 = p2.next
        
        return head

