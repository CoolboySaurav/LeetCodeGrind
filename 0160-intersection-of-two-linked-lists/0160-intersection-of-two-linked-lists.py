# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1,l2=headA,headB
        if not l1 or not l2:
            return None
        char=set()
        while l1:
            if l1 in char:
                continue
            char.add(l1)
            l1=l1.next
        while l2:
            if l2 in char:
                return l2
            l2=l2.next
        return None