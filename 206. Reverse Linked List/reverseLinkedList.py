# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Set a prev variable to None
        prev = None
        
        #Reverse linked list incorporating prev
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        return prev