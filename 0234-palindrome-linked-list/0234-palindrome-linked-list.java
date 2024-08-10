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
    public boolean isPalindrome(ListNode head) {
        ListNode p1 = head, p2 = reverse(findMid(head));
        
        while ((p2 != null) && (p1.val == p2.val)){
            p1 = p1.next;
            p2 = p2.next;
        }
        return true ? p2 == null : false;
        
    }
    
    private ListNode reverse(ListNode cur){
        ListNode prev = null, temp = null;
        
        while (cur != null){
            temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;
    }
    
    private ListNode findMid(ListNode cur){
        ListNode slow = cur, fast = cur;
        
        while ((fast != null) && (fast.next != null)){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}