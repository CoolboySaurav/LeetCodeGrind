# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur=root
        def height(cur):
                if not cur:
                    return 0
                return 1 + max(height(cur.left),height(cur.right))
        def check(cur):
            if not cur:
                return True
            l=height(cur.left)
            r=height(cur.right)
            if abs(l-r)>1:
                return False
            lh=check(cur.left)
            rh=check(cur.right)
            # if (not lh or not rh):
            #     return False
            # return True
            return lh and rh
        return check(cur)