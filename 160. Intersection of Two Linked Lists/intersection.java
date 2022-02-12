/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //If either of the head nodes are null, return null. There is no intersection
        if (headA == null || headB == null) return null;
        
        //Use a two pointer approach
        ListNode a_pointer = headA;
        ListNode b_pointer = headB;
        
        //While a does not equal b, traverse the nodes and set the end of a to the start of b and vice versa. 
        //This will account for the nodes being of different lengths
        while (a_pointer != b_pointer){
            if (a_pointer == null){
                a_pointer = headB;
            } else {
                a_pointer = a_pointer.next;
            }
            if (b_pointer == null){
                b_pointer = headA;
            } else {
                b_pointer = b_pointer.next;
            }
        }
        
        //If there is an intersection, you will be on the intersection node at this time bc of the while loop
        //So all you have to do is return either a_pointer or b_pointer
        return a_pointer;
    }
}