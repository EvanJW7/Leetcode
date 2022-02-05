# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Make a dummy linked list and use and use head to point at the head of the list
        dummy = ListNode()
        head = dummy
        
        #While both lists are still in range, iterate through them and add the lowest value to the dummy 
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            #Make sure to increment the dummy list
            dummy = dummy.next
        
        #Take care of edge cases of lists being of different lengths
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return head.next
         