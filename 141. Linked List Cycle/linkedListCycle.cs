/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
        //Make a slow and fast pointer
        ListNode slow = head;
        ListNode fast = head;
        
        //While fast and fast.next are not null...
        while (fast != null && fast.next != null){
            //Increment fast by twice the rate of slow
            fast = fast.next.next;
            slow = slow.next;
            //If there is a cycle, they will eventually equal each other
            if (slow == fast){
                return true;
            }
        }
        //If not, return false
        return false;
    }
}