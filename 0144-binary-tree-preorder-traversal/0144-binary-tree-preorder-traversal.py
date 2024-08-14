# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        cur = root
        res = []
        
        while st or cur:
            while cur:
                res.append(cur.val)
                st.append(cur)
                cur = cur.left
            cur = st.pop().right
        return res