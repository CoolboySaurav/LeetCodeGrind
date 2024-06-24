# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def travel(node, target):
            
            if not node:
                return False
            
            target -= node.val
            
            if target == 0:
                if not node.left and not node.right:
                    return True
                
            left = travel(node.left, target)
            right = travel(node.right, target)
                
            return left or right
        
        return travel(root, targetSum)
            