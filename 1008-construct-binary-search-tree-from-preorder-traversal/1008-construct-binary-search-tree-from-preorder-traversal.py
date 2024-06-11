# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def build(arr, i , bound):
            if i[0] == len(arr) or arr[i[0]] > bound:
                return None
            root = TreeNode(arr[i[0]])
            i[0] += 1
            root.left = build(arr, i, root.val)
            root.right = build(arr, i, bound)
            return root
        
        
        
        i = [0]
        
        return build(preorder, i, 1e7)