/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set <ListNode> nodeMap = new HashSet <>();
        ListNode l1 = headA, l2 = headB;
        
        while (l1 != null){
            nodeMap.add(l1);
            l1 = l1.next;
        }
        while (l2 != null){
            if (nodeMap.contains(l2)) return l2;
            l2 = l2.next;
        }
        return null;   
    }
}
