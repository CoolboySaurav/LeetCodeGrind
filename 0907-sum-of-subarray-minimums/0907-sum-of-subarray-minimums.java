import java.util.Stack;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Stack<Integer> stack = new Stack<>(); // Stack will store indices
        int res = 0;
        int mod = 1000000007; 
        
        // Find left side limits for each element being the minimum in those possible subarrays
        for (int i = 0; i < n; i++){
            // We need to create an increasing sequence inside the stack
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]){
                stack.pop();
            }
            
            left[i] = stack.isEmpty() ? i + 1 : (i - stack.peek());
            stack.push(i);
        }
        
        stack.clear(); // Clear stack for the right side calculation
        
        // Now find the right side limits for each element in a similar way
        for (int i = n - 1; i >= 0; i--){
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]){
                stack.pop();
            }
            
            right[i] = stack.isEmpty() ? (n - i) : (stack.peek() - i);
            stack.push(i);
        }
        
        // Calculate the result based on left and right limits
        for (int i = 0; i < n; i++){
            res = (res + (int)((long)arr[i] * left[i] * right[i] % mod)) % mod;
        }
        
        return res;
    }
}
