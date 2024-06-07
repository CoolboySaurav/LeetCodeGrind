# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        first=head
        second=first.next
        t=second
        while second and second.next:
            first.next=second.next
            first=first.next
            second.next=first.next
            second=second.next
        first.next=t
        return head