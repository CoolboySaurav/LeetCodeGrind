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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        //postorder(root, result);
        Stack<TreeNode> st = new Stack<>();
        TreeNode cur = root;
        
        while ((!st.isEmpty()) || (cur != null)){
            if (cur != null) {
                st.push(cur);
                cur = cur.left;
            }
            else{
                TreeNode tmp = st.peek().right;
                if (tmp == null){
                    tmp = st.pop();
                    result.add(tmp.val);
                    while ((!st.isEmpty()) && (st.peek().right == tmp)){
                        tmp = st.pop();
                        result.add(tmp.val);
                    }
                }
                else{
                    cur = tmp;
                }
            }
        }
        
        return result;
    }
    
    private void postorder(TreeNode node, List<Integer> result){
        if (node == null) return;
        
        postorder(node.left, result);
        postorder(node.right, result);
        result.add(node.val);
    }
}