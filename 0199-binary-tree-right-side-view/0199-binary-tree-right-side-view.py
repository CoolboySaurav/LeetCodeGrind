# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return None
        # Recursive Optimal Solution
        res = []
        
        def travel(node, level):
            if not node:
                return None
            
            if level == len(res):
                res.append(node.val)
            
            travel(node.right, level + 1)
            travel(node.left, level + 1)
        
        travel(root, 0)
        
        return res
        
        
        
        # Iterative sub-optimal solution
        
        # res=[]
        # q=collections.deque()
        # q.append(root)
        # cur=root
        # while q:
        #     l=len(q)
        #     level=[]
        #     for i in range(l):
        #         cur=q.popleft()
        #         if cur:
        #             level.append(cur.val)
        #             q.append(cur.left)
        #             q.append(cur.right)
        #     if level:
        #         res.append(level[-1])
        # return res