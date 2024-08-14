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
    int result = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        
        helper(root);
        return result;
    }
    
    private int helper(TreeNode node){
        if (node == null) return -1;
        int left = helper(node.left);
        int right = helper(node.right);
        result = Math.max(result, left + right + 2);
        return 1 + Math.max(left, right);
    }
}