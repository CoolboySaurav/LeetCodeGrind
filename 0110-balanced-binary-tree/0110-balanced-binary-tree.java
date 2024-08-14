/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        boolean check = false;
        if (Math.abs(left - right) <= 1) check = true;
        return (check && isBalanced(root.left) && isBalanced(root.right));
    }
    
    private int maxDepth(TreeNode node){
        if (node == null) return 0;
        int left = 1 + maxDepth(node.left);
        int right = 1 + maxDepth(node.right);
        return Math.max(left, right);
    }
}