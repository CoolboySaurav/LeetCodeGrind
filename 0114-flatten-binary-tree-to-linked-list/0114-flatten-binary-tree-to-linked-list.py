# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init(self):
        self.prev = None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        # Recursinve Solution
        def travel(node):
            if not node:
                return None
            
            travel(node.right)
            travel(node.left)
            
            node.right = self.prev
            node.left = None
            self.prev = node
        
        
        # Iterative Approach O(N) space complexity
        st = [root]
        
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            if st:
                node.right = st[-1]
            node.left = None