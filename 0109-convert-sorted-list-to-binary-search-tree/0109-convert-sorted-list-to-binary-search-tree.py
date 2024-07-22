# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        if not head:
            return None
        
        arr = []
        temp = head
        
        while temp:
            arr.append(temp)
            temp = temp.next
        
        l, r = 0, len(arr) - 1
        
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            
            node = TreeNode(arr[mid].val)
            
            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)
            return node
        
        return helper(l,r)