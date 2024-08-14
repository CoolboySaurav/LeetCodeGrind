# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = deque()
        st.append(root)
        res = []
        
        while st:
            l = len(st)
            level = []
            for i in range(l):
                node = st.popleft()
                if node:
                    level.append(node.val)
                    st.append(node.left)
                    st.append(node.right)
            if level:
                res.append(level)
        
        return res