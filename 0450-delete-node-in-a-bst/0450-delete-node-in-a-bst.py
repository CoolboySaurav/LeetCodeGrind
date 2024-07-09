# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        """
            We connect the left branch to the parent of the key node and then we find the greatest node of that left branch and connect the right branch of key node to that node's right
        """
        def findLastRight(node): # Find the last rightmost node of the given node
            if not node.right:
                return node
            return findLastRight(node.right)
        
        def helper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            right = node.right
            left = findLastRight(node.left)
            left.right = node.right
            return node.left
        
        
        
        if not root:
            return None
        
        if root.val == key:
            return helper(root)
        
        dummy = root
        
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                else:
                    root = root.right
        
        return dummy
    
    