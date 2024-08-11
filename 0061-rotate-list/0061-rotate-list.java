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
    public ListNode rotateRight(ListNode head, int k) {
        int n = findLength(head);
        if (n == 0) return null;
        k = k % n;
        k = n - k - 1;
        ListNode cur = head;
        
        while (k > 0){
            cur = cur.next;
            k--;
        }
        ListNode temp = cur.next;
        cur.next = null;
        cur = temp;
        temp = head;
        head = reverse(head);
        cur = reverse(cur);
        temp.next = cur;
        head = reverse(head);
        return head;
        
        
        
    }
    
    private int findLength(ListNode node){
        int count = 0;
        
        while (node != null){
            node = node.next;
            count++;
        }
        return count;
    }
    
    private ListNode reverse(ListNode node){
        ListNode prev = null, temp = null;
        
        while (node != null){
            temp = node.next;
            node.next = prev;
            prev = node;
            node = temp;
        }
        return prev;
    }
}