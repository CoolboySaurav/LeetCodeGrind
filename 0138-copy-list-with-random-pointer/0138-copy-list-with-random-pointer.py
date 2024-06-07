"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head is None:
            return None
          
        nodeHash = {None:None}

        temp = head

        while temp:
            copy = Node(temp.val,None,None)
            nodeHash[temp]=  copy
            temp = temp.next
        
        temp = head
        while temp:
            copy = nodeHash[temp]
            copy.next =  nodeHash[temp.next]
            copy.random = nodeHash[temp.random]
            temp = temp.next
        
        return  nodeHash[head]
