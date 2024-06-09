# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        
        def travel(node):
            if not node:
                return None
            
            travel(node.left)
            travel(node.right)
            res.append(node.val)
            
        travel(root)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]

#         lstack=[]
#         rstack=[]
#         cur=root
#         lstack.append(cur)
#         while lstack:
#             cur=lstack.pop()
#             if cur:
#                 rstack.append(cur)
#                 if cur.left:
#                     lstack.append(cur.left)
#                 if cur.right:
#                     lstack.append(cur.right)
#         while rstack:
#             cur=rstack.pop()
#             res.append(cur.val)        
                   
#         return res
        
        
        
        
        # def traverse(root):
        #     if not root:
        #         return
        #     traverse(root.left)
        #     traverse(root.right)
        #     res.append(root.val)
        #     return
        # traverse(root)
        # return res