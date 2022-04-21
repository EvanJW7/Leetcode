/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
        //Take care of edge case of first val being element we want to delete
        //This also ignores head nodes that are null
        //We want to use a while loop because there might be more than one val in a row needing deletion
        while (head != null && head.val == val){
            head = head.next;
        }
        
        ListNode curr = head;
        //While curr isn't null and there is a next element, remove element with references
        while (curr != null && curr.next != null){
            if (curr.next.val == val){
                curr.next = curr.next.next;
            }else{
                curr = curr.next;
            }
        }
        
        return head;
    }
}