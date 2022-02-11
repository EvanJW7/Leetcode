/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        //Make a slow and fast pointer
        ListNode slow = head;
        ListNode fast = head;
        
        //While fast and fast.next are not null...
        while (fast != null && fast.next != null){
            //Increment fast by twice the rate of slow
            fast = fast.next.next;
            slow = slow.next;
            //If there is a cycle, they will eventually equal eachother
            if (slow == fast){
                return true;
            }
        }
        //If not, return false, there is no cycle 
        return false;
    }
}