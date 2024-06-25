# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            L = len(q)
            number = 0.0
            
            for i in xrange(L):
                node = q.popleft()
                if node:
                    number += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(number/L)
        
        return res