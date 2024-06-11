# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(root,val):
            if not root:
                return None
            if root.val==val:
                return root
            elif root.val<val:
                return search(root.right,val)
            else:
                return search(root.left,val)
        return search(root,val)