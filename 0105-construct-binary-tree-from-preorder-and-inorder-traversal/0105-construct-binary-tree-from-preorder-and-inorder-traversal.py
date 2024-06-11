# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def traverse(preorder,prestart,preend,inorder,instart,inend,hash1):
            if instart>inend or prestart>preend:
                return None
            root=TreeNode(preorder[prestart])
            i=hash1[root.val]
            inroot=i-instart
            root.left=traverse(preorder, prestart+1, prestart+inroot, inorder, instart,i-1, hash1)
            root.right=traverse(preorder,prestart+inroot+1,preend,inorder,i+1,inend,hash1)
            return root

        hash1={element:index for index, element in enumerate(inorder)}
        root=traverse(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,hash1)
        return root
        