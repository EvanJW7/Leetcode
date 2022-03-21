# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Make a current_node to point at the head
        current_node = head
        
        #While not null, traverse and update accordingly
        while current_node:
            if current_node.next and current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        #Return the head at the end
        return head 
        