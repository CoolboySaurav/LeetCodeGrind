# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        if not head:
            return None
        def findmiddle(head):
            prev, slow, fast = None, head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        mid = findmiddle(head)
        root = TreeNode(mid.val)
        if mid == head:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    
    
        
        
        # My solution with higher memory usage via array storing linked list nodes
        if not head:
            return None
        
        arr = []
        temp = head
        
        while temp:
            arr.append(temp)
            temp = temp.next
        
        l, r = 0, len(arr) - 1
        
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            
            node = TreeNode(arr[mid].val)
            
            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)
            return node
        
        return helper(l,r)