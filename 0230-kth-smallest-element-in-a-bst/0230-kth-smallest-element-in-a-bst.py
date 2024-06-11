# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node, counter, k, k_smallest):
            if not node or counter[0] >= k:
                return

            # Traverse left subtree
            inorder(node.left, counter, k, k_smallest)

            # Increment counter after visiting left subtree
            counter[0] += 1

            # Check if current node is the Kth smallest
            if counter[0] == k:
                k_smallest[0] = node.val
                return

            # Traverse right subtree if
            # Kth smallest is not found yet
            inorder(node.right, counter, k, k_smallest)

        k_smallest = [1e7]
        counter = [0]
        inorder(root, counter, k, k_smallest)
        return k_smallest[0]
        
        
        
        
        # if not root:
        #     return None
        # n=0
        # stack=[]
        # cur=root
        # while cur and stack:
        #     while cur:
        #         stack.append(cur)
        #         cur=cur.left
        #     cur=stack.pop()
        #     n+=1
        #     if n==k:
        #         return cur.val
        #     cur=cur.right
        # res=[]
        # def traverse(node,k):
        #     if not node:
        #         return None
        #     traverse(node.left,k)
        #     res.append(node.val)
        #     traverse(node.right,k)
        # traverse(root,k)
        # return res[k-1]