# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        
        res = []
        q = deque()
        q.append(root)
        
        leftToRight = True
        
        while q:
            L = len(q)
            level = [0]*L
            
            for i in xrange(L):
                curr = q.popleft()
                if curr:
                    if leftToRight:
                        index = i
                    else:
                        index = L - i - 1

                    level[index] = curr.val

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            leftToRight = not leftToRight
            if level:
                res.append(level)
        
        return res