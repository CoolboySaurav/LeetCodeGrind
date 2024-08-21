# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        self.helper(root, count, root.val)
        return count[0]
    def helper(self, node, count, maxValue):
        if not node:
            return
        if node.val >= maxValue:
            count[0] += 1
            self.helper(node.left, count, node.val)
            self.helper(node.right, count, node.val)
        else:
            self.helper(node.left, count, maxValue)
            self.helper(node.right, count, maxValue)
        