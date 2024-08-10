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
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return head;
        
        ListNode p1 = head, temp = null, p2 = head.next, p3 = p2;
        
        while (p2 != null){
            p1.next = p2.next;
            if (p1.next == null){
                p1.next = p2;
                break;
            }
            p1 = p1.next;
            p2.next = p1.next;
            p2 = p2.next;
        }
        p1.next = p3;
        return head;
    }
}