# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        st = []
        cur = root
        
        while st or cur:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                tmp = st[-1].right
                if not tmp:
                    tmp = st.pop()
                    res.append(tmp.val)
                    while st and st[-1].right == tmp:
                        tmp = st.pop()
                        res.append(tmp.val)
                else:
                    cur = tmp
                
        return res
        