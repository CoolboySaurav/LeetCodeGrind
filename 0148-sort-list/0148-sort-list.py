# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        left=head
        right=self.getMid(head)
        temp=right.next
        right.next=None
        right=temp

        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)

    def getMid(self,node):
        slow=fast=node
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def merge(self,left,right):
        temp=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        if left:
            temp.next=left
        elif right:
            temp.next=right
        return dummy.next
        