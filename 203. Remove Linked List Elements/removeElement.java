class Solution {
    public ListNode removeElements(ListNode head, int val) {
        //Take care of case when val is the first node
        //You must use a while loop because it might repeat more than once
        while (head != null && head.val == val){
            head = head.next;
        }
        ListNode current_node = head;
        while(current_node != null && current_node.next != null){
            //If the next node is the node we want to remove, skip over it
            if (current_node.next.val == val){
                current_node.next = current_node.next.next;
            }
            //If it's not something we want to remove, continue with regular traversal
            else{
                current_node = current_node.next;
            }
        }
      return head;
        
    }
}