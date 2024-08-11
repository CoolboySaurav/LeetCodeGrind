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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int total = 0, carry = 0;
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        
        while ((l1 != null) || (l2 != null)){
            total = carry;
            if (l1 != null){
                total += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                total += l2.val;
                l2 = l2.next;
            }
            carry = total / 10;
            total = total % 10;
            temp.next = new ListNode(total);
            temp = temp.next;
        }
        if (carry != 0){
            temp.next = new ListNode(carry);
        }
        return dummy.next;    
    
        
    }
}