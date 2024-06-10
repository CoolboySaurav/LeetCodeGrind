# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def leftHeight(self, node):

            count =0
            while node:
                count += 1
                node = node.left
            
            return count
        
    def rightHeight(self, node):

            count = 0
            while node:
                count += 1
                node = node.right
            
            return count

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
                    
        if not root:
            return 0

        left = self.leftHeight(root)
        right = self.rightHeight(root)

        if left == right:
            return (2**left) - 1
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
#         def travel(node):
#             if not node:
#                 return 0
            
#             l = travel(node.left)
#             r = travel(node.right)
            
#             return 1 + l + r
        
#         return travel(root)
        
        