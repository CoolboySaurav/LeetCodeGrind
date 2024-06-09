# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur=root
        def height(cur):
            if not cur:
                return 0
            l=height(cur.left)
            r=height(cur.right)
            return 1+ max(l,r)
        return height(root)