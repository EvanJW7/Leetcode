class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //Make a dummy linked list
        ListNode dummy = new ListNode();
        //Use a node called head to point to the head of the dummy
        ListNode head = dummy;
        
        //Go through each element of the lists while both of them are not null
        while (list1 != null && list2 != null){
            if (list1.val < list2.val){
                dummy.next = list1;
                list1 = list1.next;
            }
            else{
                dummy.next = list2;
                list2 = list2.next;
            }
            //Make sure to increment dummy
            dummy = dummy.next;
        }
        //Add the ends of the non-null lists if needed
        if (list1 != null){
            dummy.next = list1;
        }
        else{
            dummy.next = list2;
        }
        
        return head.next;
    }
}