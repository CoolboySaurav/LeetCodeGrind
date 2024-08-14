# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        cur = root
        res = []
        while st or cur:
            while cur:
                st.append(cur)
                cur = cur.left
            res.append(st[-1].val)
            cur = st.pop().right
        return res