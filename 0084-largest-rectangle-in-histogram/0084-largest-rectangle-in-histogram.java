
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Pair<Integer, Integer>> st = new Stack<>();
        int maxArea = 0;
        int n = heights.length;
        
        for (int i = 0; i < n; i++) {
            int start = i;
            while (!st.isEmpty() && st.peek().getValue() > heights[i]) {
                Pair<Integer, Integer> pair = st.pop();
                int height = pair.getValue();
                int width = i - pair.getKey();
                maxArea = Math.max(maxArea, height * width);
                start = pair.getKey();
            }
            st.push(new Pair<>(start, heights[i]));
        }
        
        // Process any remaining elements in the stack
        while (!st.isEmpty()) {
            Pair<Integer, Integer> pair = st.pop();
            int height = pair.getValue();
            int width = n - pair.getKey();
            maxArea = Math.max(maxArea, height * width);
        }
        
        return maxArea;
    }
}
