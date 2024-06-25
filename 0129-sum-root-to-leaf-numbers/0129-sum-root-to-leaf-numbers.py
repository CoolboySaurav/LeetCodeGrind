# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.result = 0
    
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def calculate(node, currSum):
            if not node:
                return 
            
            if not node.left and not node.right:
                self.result += currSum*10 + node.val
                return 
            
            currSum = currSum*10 + node.val
            calculate(node.left, currSum)
            calculate(node.right, currSum)
        
        calculate(root, 0)
        
        return self.result
        