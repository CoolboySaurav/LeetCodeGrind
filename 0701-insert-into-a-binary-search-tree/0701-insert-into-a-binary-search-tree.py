# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # Recursive Solution
        
        # def insert(root,val):
        #     if not root:
        #         return TreeNode(val)
        #     elif root.val==val:
        #         return root
        #     elif root.val<val:
        #         root.right=insert(root.right,val)
        #     else:
        #         root.left=insert(root.left,val)
        #     return root
        # return insert(root,val)
        
        # Iterative Solution
        
        if not root:
            return TreeNode(val)
        cur = root
        
        while cur:
            if cur.val >= val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        
        return root
        
        
        
        
        # q=collections.deque()
        # q.append(root)
        # level=[]
        # res=[]
        # while q:
        #     level=[]
        #     qlen=len(q)
        #     for i in range(qlen):
        #         cur=q.popleft()
        #         if cur:
        #             level.append(cur.val)
        #             q.append(cur.left)
        #             q.append(cur.right)
        #     if level:
        #         for i in level:
        #             res.append(i)
        # return res
                

