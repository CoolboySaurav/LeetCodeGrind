
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums2.length;
        Map<Integer, Integer> num = new HashMap<>();
        Stack<Integer> st = new Stack<>();
        
        if(nums1.length == 0 || n == 0) return new int[0];
        
        for (int i = n - 1; i >= 0; i--) {
            int element = nums2[i];
            
            // Pop elements from the stack that are less than or equal to the current element
            while (!st.isEmpty() && st.peek() <= element) {
                st.pop();
            }
            
            // If the stack is empty, no greater element exists
            if (st.isEmpty()) {
                num.put(element, -1);
            } else {
                // The next greater element is the top of the stack
                num.put(element, st.peek());
            }
            
            // Push the current element onto the stack
            st.push(element);
        }
        
        // Replace elements in nums1 with their corresponding next greater element
        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = num.get(nums1[i]);
        }
        
        return nums1;
    }
}