# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevNode = None
        temp = head
        
        while temp:
            kthNode = self.getKthNode(temp, k)
            if not kthNode:
                prevNode.next = temp
                break
            nxtNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nxtNode
        return head
    
    def reverse(self, node):
        prev = temp = None
        
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
    
    def getKthNode(self, node, k):
        k -= 1
        
        while node and k > 0:
            k -= 1
            node = node.next
        
        return node
        