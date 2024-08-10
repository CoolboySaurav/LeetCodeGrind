/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        
        // Detect if there is a cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                // There is a cycle; find the start of the cycle
                ListNode slow1 = head;
                while (slow1 != slow) {
                    slow1 = slow1.next;
                    slow = slow.next;
                }
                return slow1; // Start of the cycle
            }
        }
        
        // No cycle
        return null;
    }
}
