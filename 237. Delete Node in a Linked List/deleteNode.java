/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        //Set the value of our node to the value of the node after it
        node.val = node.next.val;
        //Then delete the reference to the subsequent node
        node.next = node.next.next;
    }
}