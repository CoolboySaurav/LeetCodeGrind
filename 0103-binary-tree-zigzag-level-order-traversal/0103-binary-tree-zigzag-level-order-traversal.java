import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        boolean leftToRight = true;
        Queue<TreeNode> q = new LinkedList<>();
        if (root != null) q.add(root);
        List<List<Integer>> res = new ArrayList<>();
    
        while (!q.isEmpty()){
            int len = q.size();
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < len; i++){
                TreeNode node = q.poll();
                
                // Add node value to the level list
                if (leftToRight) {
                    level.add(node.val);
                } else {
                    level.add(0, node.val); // Add to the beginning of the list
                }
                
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            
            // Toggle the direction
            leftToRight = !leftToRight;
            res.add(level);
        }
        return res;
    }
}
