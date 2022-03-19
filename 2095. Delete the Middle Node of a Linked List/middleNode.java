/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        //Make a dummy node to traverse the linked list
        ListNode dummy = new ListNode();
        //Make dummy equal to head. Make sure to say dummy.next otherwise the first element won't be included
        dummy.next = head;
        //Make a slow and fast pointer
        ListNode slow = dummy;
        ListNode fast = dummy;
        //When the fast pointer reaches null, the slow pointer will be in the middle of the list
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //Now that we are in the middle of the list, we skip the next node
        slow.next = slow.next.next;
        //Return the dummy linked list since that is what we were modifying 
        return dummy.next;
        
        
    }
}