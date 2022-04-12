/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    //create a struct ListNode, and then use a pointer to it
    struct ListNode head;
    struct ListNode *h = &head;
    
    while(list1 != NULL && list2 != NULL){
        if (list1->val < list2->val){
            h->next = list1;
            list1 = list1->next;
        }else{
            h->next = list2;
            list2 = list2->next;
        }
        h = h->next;
    }
    
    if (list1 != NULL){h->next = list1;}
    else{h->next = list2;}
    
    return head.next;

}
