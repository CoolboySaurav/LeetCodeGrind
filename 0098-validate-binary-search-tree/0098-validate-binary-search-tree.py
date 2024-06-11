# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def fact(node,left,right):
            if not node:
                return True
            if not ((node.val>left and node.val<right)):
                return False
            return (fact(node.left,left,node.val) and fact(node.right,node.val,right))
        
        return fact(root,float("-inf"),float("inf"))