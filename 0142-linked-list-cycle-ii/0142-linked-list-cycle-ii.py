# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow=fast=slow1=head
        while fast and fast.next:
            if fast is None:
                return None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=slow1:
                    slow=slow.next
                    slow1=slow1.next   
                return slow
        return None
            
        