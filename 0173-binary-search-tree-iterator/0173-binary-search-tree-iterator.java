import java.util.Stack;

class BSTIterator {

    private Stack<TreeNode> st;  // Declare stack as an instance variable

    public BSTIterator(TreeNode root) {
        st = new Stack<>();  // Initialize the stack
        extract(root);  // Populate the stack with the leftmost nodes
    }
    
    private void extract(TreeNode node) {
        while (node != null) {
            st.push(node);  // Push current node onto the stack
            node = node.left;  // Move to the left child
        }
    }
    
    public int next() {
        TreeNode node = st.pop();  // Pop the top node from the stack
        if (node.right != null) {
            extract(node.right);  // If right child exists, process its left subtree
        }
        return node.val;  // Return the value of the popped node
    }
    
    public boolean hasNext() {
        return !st.isEmpty();  // Return true if the stack is not empty
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
