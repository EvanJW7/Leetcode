/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    //Make a pointer to the head so you can traverse
    struct ListNode* current_node = head;
    //Edge case: linked list has no elements
    if (current_node == NULL) return head;
    
    while (current_node->next != NULL){
        if (current_node->val == current_node->next->val){
            current_node->next = current_node->next->next;
        }else{
            current_node = current_node->next;
        }
    }
    return head;  
    }
