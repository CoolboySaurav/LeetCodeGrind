# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        def find(node, parent, val, depth):
            if not node:
                return [-1, depth]
            if node.val == val:
                return [parent, depth + 1]
            
            left = find(node.left, node, val, depth + 1)
            right = find(node.right, node, val, depth + 1)
            
            if left[0] != -1:
                return left
            else:
                return right
            
        left = find(root, -1, x, 0)
        right = find(root, -1,y, 0)
        
        if left[0] != right[0] != -1 and left[1] == right[1]:
            return True
        else:
            return False