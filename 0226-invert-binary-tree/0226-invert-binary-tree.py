# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def travel(node):
            if not node:
                return None
            left = travel(node.left)
            right = travel(node.right)
            node.left = right
            node.right = left
            return node
        
        travel(root)
        return root       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         temp=None
#         def inv(root):
#             if not root:
#                 return None
#             temp=root.left
#             root.left=root.right
#             root.right=temp
#             inv(root.left)
#             inv(root.right)
#             return root
#         return inv(root)
        