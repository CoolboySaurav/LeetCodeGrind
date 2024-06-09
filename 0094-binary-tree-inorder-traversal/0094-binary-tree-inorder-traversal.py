# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Recursion Solution
        
#         if not root:
#             return None
        
#         res = []
        
#         def travel(node):
#             if not node:
#                 return 
            
#             travel(node.left)
#             res.append(node.val)
#             travel(node.right)
        
#         travel(root)
#         return res
        
        
        # Iterative Solution
        
        res=[]
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res


