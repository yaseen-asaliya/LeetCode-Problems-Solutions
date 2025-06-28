# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_node = list1  
        b_node = None  

        for x in range(a-1):
            a_node = a_node.next

        b_node = a_node

        for x in range((b-a)+2):
            b_node = b_node.next
            
        a_node.next = list2

        temp = list2
        while temp.next:
            temp = temp.next
        
        temp.next = b_node

        return list1