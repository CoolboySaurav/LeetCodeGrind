import java.util.ArrayList;
import java.util.List;

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
    
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        //preorder(root, result);
        Stack <TreeNode> st = new Stack<>();
        TreeNode cur = root;
        
        while ((!st.isEmpty()) || (cur != null)){
            while (cur != null){
                result.add(cur.val);
                st.push(cur);
                cur = cur.left;
            }
            cur = st.peek().right;
            st.pop();
        }
        
        return result;
    }
    
    private void preorder(TreeNode node, List<Integer> result) {
        if (node == null) return;
        
        result.add(node.val); // Visit the root
        preorder(node.left, result); // Traverse left subtree
        preorder(node.right, result); // Traverse right subtree
    }
}
