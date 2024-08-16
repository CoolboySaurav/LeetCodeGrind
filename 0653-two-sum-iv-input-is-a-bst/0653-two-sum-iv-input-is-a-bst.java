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
    public boolean findTarget(TreeNode root, int k) {
        if (root == null) return false;
        return helper(root, k, new HashMap<>());
    }
    private boolean helper(TreeNode node, int k, HashMap<Integer, Integer> map){
        if (node == null) return false;
        if (map.containsKey(k - node.val)) return true;
        map.put(node.val, 1);
        return helper(node.left, k, map) || helper(node.right, k, map);
    }
}