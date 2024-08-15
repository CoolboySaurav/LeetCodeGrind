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
    public int widthOfBinaryTree(TreeNode root) {
        Queue <Pair<TreeNode, Integer>> queue = new ArrayDeque<>();
        queue.offer(new Pair<>(root, 0));
        int maxLen = 0;
        
        while (!queue.isEmpty()){
            int L = queue.size();
            int first = 0, last = 0;
            int minIndex = queue.peek().getValue();
            
            for (int i = 0; i < L; i++){
                
                int cur_id = queue.peek().getValue() - minIndex;
                
                TreeNode node = queue.peek().getKey();
                queue.poll();
                
                if (i == 0) first = cur_id;
                if (i == L - 1) last = cur_id;
                
                if (node.left != null) queue.offer(new Pair<>(node.left, 2* cur_id + 1));
                if (node.right != null) queue.offer(new Pair<>(node.right, 2*cur_id + 2));
            }
            maxLen = Math.max(maxLen, (last - first + 1));
        }
        
        return maxLen;
    }
}