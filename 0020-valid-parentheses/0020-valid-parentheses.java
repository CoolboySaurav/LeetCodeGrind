import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> bracket = new HashMap<>();
        bracket.put(')', '(');
        bracket.put(']', '[');
        bracket.put('}', '{');
        Stack<Character> st = new Stack<>();

        for (char c : s.toCharArray()) {
            if (!bracket.containsKey(c)) {
                st.push(c);  // Use push instead of add for a stack
            } else {
                if (st.isEmpty() || st.pop() != bracket.get(c)) {
                    return false;
                }
            }
        }
        
        return st.isEmpty();
    }
}
