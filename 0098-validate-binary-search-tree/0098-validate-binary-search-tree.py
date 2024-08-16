# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.helper(root, float('-inf'), float('inf'))
    def helper(self, node, leftBound, rightBound):
        if not node: return True
        if node.val <= leftBound or node.val >= rightBound:
            return False
        return self.helper(node.left, leftBound, node.val) and self.helper(node.right, node.val, rightBound)