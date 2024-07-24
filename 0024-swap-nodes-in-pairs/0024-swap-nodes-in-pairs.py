# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy=ListNode(0,head)
        # prev,curr=dummy,head
        # while curr and curr.next:
        #     nxtPair=curr.next.next
        #     second=curr.next
        #     #reverse
        #     second.next=curr
        #     curr.next=nxtPair
        #     prev.next=second
        #     #update pointers
        #     prev=curr
        #     curr=nxtPair
        # return dummy.next
        if head is None or head.next is None:
            return head
        t=head.next.next
        start=self.swap(head)
        end=start.next
        end.next=self.swapPairs(t)
        return start
        
    def swap(self,head):
        if head is None or head.next is None:
            return head
        prev=None
        temp=head.next
        head.next=prev
        temp.next=head
        return temp

        
        
        
        
        