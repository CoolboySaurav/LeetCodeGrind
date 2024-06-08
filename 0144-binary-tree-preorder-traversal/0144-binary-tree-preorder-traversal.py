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
        res = []
        
        def travel(node):
            if not node:
                return 
            
            res.append(node.val)
            travel(node.left)
            travel(node.right)
        
        travel(root)
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