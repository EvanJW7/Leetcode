class Solution {
    public ListNode reverseList(ListNode head) {
        //Make a null node so you can reference it (backwards)
        ListNode prev = null;
        
        //Make a while loop
        while (head != null){
            //Make a new node so you can reference it (forwards)
            ListNode next_node = head.next;
            //Point the beginning of the array to null
            head.next = prev;
            //Move prev to current node
            prev = head;
            //Move head to the next node 
            head = next_node;
        }
        return prev;
    }
}
