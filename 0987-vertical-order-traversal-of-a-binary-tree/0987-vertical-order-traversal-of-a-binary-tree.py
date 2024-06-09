# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = defaultdict(lambda: defaultdict(list))
        q = deque()
        q.append([root, (0,0)])
        
        while q:
            temp , (x,y) = q.popleft()
            
            nodes[x][y].append(temp.val)
            
            if temp.left:
                q.append([temp.left,(x-1,y+1)])
            if temp.right:
                q.append([temp.right, (x+1,y+1)])
            
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)

        return ans
            
        