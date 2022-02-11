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
    public ListNode deleteDuplicates(ListNode head) {
        //Make a pointer pointing to the head
        ListNode current_node = head;
        
        //While the current_node is not null, traverse and delete any duplicates
        while(current_node != null && current_node.next != null){
            if (current_node.val == current_node.next.val){
                current_node.next = current_node.next.next;
            }else{
            //Make sure you have an else statement in here otherwise it won't work
            current_node = current_node.next;
            }
        }
        return head;
    }
}