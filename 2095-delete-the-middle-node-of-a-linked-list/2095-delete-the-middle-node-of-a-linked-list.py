# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre=slow=fast=head
        if head.next:
            while fast and fast.next:
                pre=slow
                slow=slow.next
                fast=fast.next.next
            pre.next=slow.next
            return head
        elif not head.next:##Single element case
            return head.next
        else:
            return head