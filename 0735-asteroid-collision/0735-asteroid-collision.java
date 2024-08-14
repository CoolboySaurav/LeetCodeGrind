import java.util.Stack;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        
        for (int a : asteroids) {
            // Process the current asteroid
            while (!stack.isEmpty() && stack.peek() > 0 && a < 0) {
                int top = stack.peek();
                if (top < -a) {
                    stack.pop(); // Remove the top asteroid as it is destroyed
                } else if (top == -a) {
                    stack.pop(); // Both asteroids are destroyed
                    a = 0; // Set to 0 as current asteroid is also destroyed
                } else {
                    a = 0; // Current asteroid is destroyed
                }
            }
            if (a != 0) {
                stack.push(a); // Add remaining asteroid to the stack
            }
        }
        int ansArr[] = new int [stack.size()];
        for(int i=stack.size()-1;i>=0;i--){
            ansArr[i] = stack.pop();
        }
        return ansArr;
    }
}
