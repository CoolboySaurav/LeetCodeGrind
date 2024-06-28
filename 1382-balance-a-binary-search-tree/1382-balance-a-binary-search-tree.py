# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        res = []
        # Inorder Traversal to obtain the sorted array for the given BST
        
        def travel(node):
            if not node:
                return None
            
            travel(node.left)
            res.append(node.val)
            travel(node.right)
        
        travel(root)
        
        # Build a Balanced Binary Tree from the given sorted array
        l, r = 0, len(res) - 1
        
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(res[mid])
            root.left = build(left, mid - 1)
            root.right = build( mid + 1, right)
            return root
        
        return build(l,r)