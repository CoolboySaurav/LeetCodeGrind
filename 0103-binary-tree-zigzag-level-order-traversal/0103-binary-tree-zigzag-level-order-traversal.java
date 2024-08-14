import java.util.Collections;
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
        boolean left = true;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> res = new ArrayList<>();
    
        while (!q.isEmpty()){
            int Len = q.size();
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < Len; i++){
                TreeNode node = q.poll();
                
                if (node != null){
                    level.add(node.val);
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            if (level.isEmpty()) break;
            if (!left){
                Collections.reverse(level);
            }
            left = !left;
            res.add(level);
        }
        return res;
    }
}