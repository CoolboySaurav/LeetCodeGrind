# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subroot:
            return True
        if self.isSameTree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
    def isSameTree(self, m, n):
        if not m and not n:
            return True
        if (not m or not n) or (m.val != n.val):
            return False
        if m.val == n.val:
            return self.isSameTree(m.left, n.left) and self.isSameTree(m.right, n.right)