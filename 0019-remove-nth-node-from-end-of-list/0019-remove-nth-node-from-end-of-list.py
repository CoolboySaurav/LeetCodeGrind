# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # i=0
        # og_head=head
        # while head:
        #     i+=1
        #     head=head.next
        # head=og_head
        # i=i-n
        # j=0
        # if i<0: return og_head
        # if i==0: return og_head.next
        # while head.next:
        #     j+=1
        #     if j==i and j!=0:
        #         head.next=head.next.next
        #         return og_head
        #     head=head.next        
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
        
        