# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        q = deque()
        q.append([root,0])
        maxW = 0
        
        while q:
            indMin = q[0][1]
            first = last = 0
            L = len(q)
            
            for i in xrange(L):
                node, curInd = q.popleft()
                curInd -= indMin
                if i == 0:
                    first = curInd
                elif i == L - 1:
                    last = curInd
                
                if node.left:
                    q.append([node.left,(2*curInd + 1)])
                if node.right:
                    q.append([node.right, (2*curInd + 2)])
            maxW = max(maxW, last - first + 1)
            
        return maxW
        
        
        
#         q=collections.deque()
#         q.append([root,1,0])
#         prevlev,prevnum=0,1
#         res=0
#         while q:
#             cur,num,lev=q.popleft()
#             if prevlev<lev:
#                 prevlev=lev
#                 prevnum=num
#             res=max(res, num-prevnum+1)

#             if cur.left:
#                 q.append([cur.left,2*num,lev+1])
#             if cur.right:
#                 q.append([cur.right,2*num+1,lev+1])
#         return res

            

        


                
        