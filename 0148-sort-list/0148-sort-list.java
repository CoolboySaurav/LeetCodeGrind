class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // Find the middle of the list
        ListNode mid = findMid(head);
        ListNode left = head;
        ListNode right = mid.next;
        mid.next = null; // Split the list into two halves

        // Sort each half
        left = sortList(left);
        right = sortList(right);

        // Merge the sorted halves
        return merge(left, right);
    }
    
    private ListNode merge(ListNode left, ListNode right) {
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        
        while (left != null && right != null) {
            if (left.val <= right.val) {
                temp.next = left;
                left = left.next;
            } else {
                temp.next = right;
                right = right.next;
            }
            temp = temp.next;
        }
        
        // Append the remaining nodes
        temp.next = (left != null) ? left : right;
        return dummy.next;
    }

    private ListNode findMid(ListNode node) {
        ListNode slow = node;
        ListNode fast = node;
        
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
}
