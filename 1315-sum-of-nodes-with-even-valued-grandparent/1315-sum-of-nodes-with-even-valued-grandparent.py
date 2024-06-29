# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def traverse(node, parent, grandParent):
            if not node:
                return 0
            
            res = 0
            
            if grandParent and grandParent.val % 2 == 0:
                res += node.val
            
            return res + traverse(node.left, node, parent) + traverse(node.right, node, parent)
        
        return traverse(root, None, None)