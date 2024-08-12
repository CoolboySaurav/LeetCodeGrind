import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generate(0, 0, "", result, n);
        return result;
    }
    
    private void generate(int open, int close, String path, List<String> result, int n) {
        // Base Case
        if (path.length() == 2 * n) {
            result.add(path);
            return;
        }
        
        // Add '(' if there are remaining open parentheses to add
        if (open < n) {
            generate(open + 1, close, path + "(", result, n);
        }
        
        // Add ')' if it doesn't exceed the number of open parentheses
        if (close < open) {
            generate(open, close + 1, path + ")", result, n);
        }
    }
}
