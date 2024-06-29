# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.total = 0
        
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def travel(node):
            if not node:
                return None
            
            travel(node.right)
            self.total += node.val
            node.val = self.total
            travel(node.left)
            
        
        travel(root)
        return root