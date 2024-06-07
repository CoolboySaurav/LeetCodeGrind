# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(ptr):
            pre = None
            nex = None
            while ptr != None:
                nex = ptr.next
                ptr.next = pre
                pre = ptr
                ptr = nex
            return pre
        if not head or not head.next:
            return True
        fast=curr=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            curr=curr.next
        curr.next=reverse(curr.next)
        curr=curr.next
        dummy=head
        while curr != None:
            if dummy.val != curr.val:
                return False
            dummy = dummy.next
            curr = curr.next
        return True
            
        