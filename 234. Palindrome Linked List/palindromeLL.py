# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        output = []
        #Go through the linked list, add each val to an array and check if it is the same reversed
        while head:
            output.append(head.val)
            head = head.next
        
        return output == output[::-1]
        