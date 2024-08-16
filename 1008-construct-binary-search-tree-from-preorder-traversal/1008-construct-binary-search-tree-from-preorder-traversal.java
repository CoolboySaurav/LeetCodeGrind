class Solution {
    private int index = 0;  // Class-level variable to keep track of the current index

    public TreeNode bstFromPreorder(int[] preorder) {
        return builder(preorder, Long.MAX_VALUE);
    }

    private TreeNode builder(int[] preorder, long bound) {
        if (index >= preorder.length || preorder[index] > bound) return null;
        
        TreeNode node = new TreeNode(preorder[index++]);
        node.left = builder(preorder, node.val);
        node.right = builder(preorder, bound);
        return node;
    }
}
