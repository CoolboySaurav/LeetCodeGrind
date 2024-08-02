# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        prev, cur = None, head
        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        nodeBeforeLeft = prev
        endOfReversedLL = cur
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if nodeBeforeLeft:
            nodeBeforeLeft.next = prev
        else:
            head = prev
        endOfReversedLL.next = cur
        return head
        
        
        
        if not head or not head.next:
            return head
        dummy=ListNode(0,head)
        lprev,curr=dummy,head
        for i in range(left-1):
            lprev,curr=curr,curr.next
        last=curr
        prev=temp=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        lprev.next=prev
        last.next=curr
        return dummy.next