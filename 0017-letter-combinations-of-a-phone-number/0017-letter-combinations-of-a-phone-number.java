import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> letterCombinations(String digits) {
        // Create and populate the phone map
        Map<Character, String> phone = new HashMap<>();
        phone.put('2', "abc");
        phone.put('3', "def");
        phone.put('4', "ghi");
        phone.put('5', "jkl");
        phone.put('6', "mno");
        phone.put('7', "pqrs");
        phone.put('8', "tuv");
        phone.put('9', "wxyz");

        List<String> result = new ArrayList<>();

        // Base case
        if (digits == null || digits.length() == 0) return result;

        // Start the recursion
        helper(0, digits, result, "", phone);

        return result; // Return the result list
    }

    private void helper(int index, String digits, List<String> result, String path, Map<Character, String> phone) {
        // Base Case
        if (index == digits.length()) {
            result.add(path);
            return;
        }

        // Get the letters corresponding to the current digit
        String letters = phone.get(digits.charAt(index));

        for (char c : letters.toCharArray()) {
            // Recursive call with updated path
            helper(index + 1, digits, result, path + c, phone);
        }
    }
}
