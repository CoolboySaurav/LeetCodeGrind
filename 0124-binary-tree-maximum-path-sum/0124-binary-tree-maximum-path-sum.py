# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxi = [-1e7]
        
        def maxSum(node, maxi):
            if not node:
                return 0
            
            leftSum = max(0, maxSum(node.left, maxi))
            rightSum = max(0, maxSum(node.right, maxi))
            
            maxi[0] = max(maxi[0], (node.val + leftSum + rightSum))
            
            return node.val + max(leftSum, rightSum)
        
        maxSum(root, maxi)
        
        return maxi[0]
