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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode temp = head;
        ListNode prevNode = null;
        
        while (temp != null){
            ListNode kthNode = getkthNode(temp, k);
            if (kthNode == null){
                prevNode.next = temp;
                break;
            }
    
            ListNode nxtNode = kthNode.next;
            kthNode.next = null;
            reverse(temp);
            if (temp == head) head = kthNode;
            else{
                prevNode.next = kthNode;    
            }
            prevNode = temp;
            temp = nxtNode;
        }
        return head;
        
    }
    
    private void reverse(ListNode node){
        ListNode prev = null, temp = null;
        
        while (node != null){
            temp = node.next;
            node.next = prev;
            prev = node;
            node = temp;
        }
    }
    private ListNode getkthNode(ListNode node, int k){
        k--;
        
        while ((node != null) && (k > 0)){
            k--;
            node = node.next;
        }
        return node;
    }
}