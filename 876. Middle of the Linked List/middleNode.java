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
    public ListNode middleNode(ListNode head) {
        //Make two pointers
        ListNode slow = head;
        ListNode fast = head;
        //When fast becomes null, slow will be in the middle of the list
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        //Now we can just return slow;
        return slow;
        
    }
}