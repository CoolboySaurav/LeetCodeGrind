# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse(node):
            prev = None
            curr = temp = node
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
            
        carry = 0
        tot = 0
        curSum = 0
        temp = res = ListNode()
        
        while l1 and l2:
            curSum = l1.val + l2.val + carry
            tot = curSum % 10
            carry = int(curSum/10)
            temp.next = ListNode(tot, temp.next)
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curSum = l1.val + carry
            tot = curSum % 10
            carry = int(curSum/10)
            temp.next = ListNode(tot, temp.next)
            l1 = l1.next
        
        while l2:
            curSum = l2.val + carry
            tot = curSum % 10
            carry = int(curSum/10)
            temp.next = ListNode(tot, temp.next)
            l2 = l2.next
        
        if carry:
            temp.next = ListNode(carry, temp.next)
        
        return reverse(res.next)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         carry=0
#         tot=0
#         def reverseLL(head):
#             if not head or not head.next:
#                 return  head
#             temp=prev=None
#             curr=head
#             while curr:
#                 temp=curr.next
#                 curr.next=prev
#                 prev=curr
#                 curr=temp
#             return prev
#         if not l1:
#             return l2
#         elif not l2:
#             return l1
#         #l1=reverseLL(l1)
#         #l2=reverseLL(l2)
#         dummy=ListNode()
#         temp=dummy
#         while l1 and l2:
#             a=l1.val
#             b=l2.val
#             tot=(a+b+carry)%10
#             carry=(a+b+carry)//10
#             temp.next=ListNode(tot,temp.next)
#             l1=l1.next
#             l2=l2.next
#         if l1:
#             while l1:
#                 tot=(l1.val+carry)%10
#                 carry=(l1.val+carry)//10
#                 temp.next=ListNode(tot,temp.next)
#                 l1=l1.next
                
#         elif l2:
#             while l2:
#                 tot=(l2.val+carry)%10
#                 carry=(l2.val+carry)//10
#                 temp.next=ListNode(tot,temp.next)
#                 l2=l2.next
#         if carry>0:
#             temp.next=ListNode(carry,temp.next)
#         p=dummy.next
#         p=reverseLL(p)
#         return p   
