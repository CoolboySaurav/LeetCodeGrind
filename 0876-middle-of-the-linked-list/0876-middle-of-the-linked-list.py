# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        
        temp = head
        
        while temp:
            length += 1
            temp = temp.next

        if length % 2:
            mid = int(length / 2)
        else:
            mid = length/2 
        
        temp = head
        
        while mid > 0:
            temp = temp.next
            mid -= 1        
        
        return temp
        
        
        
        # i=0
        # curr=head
        # while curr:
        #     curr=curr.next
        #     i+=1
        # i=i//2
        # j=0
        # curr=head
        # if i%2:
        #     while j<i:
        #         curr=curr.next
        #         j+=1
        # else:
        #     while j!=i:
        #         curr=curr.next
        #         j+=1
        # return curr

        