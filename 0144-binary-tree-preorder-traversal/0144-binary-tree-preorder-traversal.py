# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Recursion way
#         res = []
        
#         def travel(node):
#             if not node:
#                 return 
            
#             res.append(node.val)
#             travel(node.left)
#             travel(node.right)
        
#         travel(root)
#         return res
        
        if not root:
            return None
        
        res = []
        stack = []
        stack.append(root)
        
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return res
        
        
        
        
        
        # res=[]
        # stack=[]
        # cur=root
        # while cur or stack:
        #     if cur:
        #         res.append(cur.val)
        #         stack.append(cur.right)
        #         cur=cur.left
        #     else:
        #         cur=stack.pop()
        # return res        
            
            
            
            
            # while cur:
            #     stack.append(cur)
            #     cur=cur.left
            # cur=cur.right
            # stack.append(cur)
            # while stack:
            #     cur=stack.pop(0)
            #     res.append(cur.val)
            #     if 
            # cur=cur.right




        # def traverse(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     traverse(root.left)
        #     traverse(root.right)
        # traverse(root)
        # return res