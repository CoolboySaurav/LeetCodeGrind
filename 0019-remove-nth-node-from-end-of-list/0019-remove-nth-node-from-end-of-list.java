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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode left = dummy, right = findnode(head, n);
        
        while (right != null){
            left = left.next;
            right = right.next;
        }
        left.next = left.next.next;
        return dummy.next;
    }
    private ListNode findnode(ListNode cur, int k){
        while ((cur != null) && (k > 0)){
            cur = cur.next;
            k--;
        }
        return cur;
    }
}