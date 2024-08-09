import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();

        // Add the first row
        result.add(new ArrayList<>(List.of(1)));
        
        for (int i = 1; i < numRows; i++) {
            List<Integer> level = new ArrayList<>();
            List<Integer> previousRow = result.get(i - 1);

            // First element of each row is 1
            level.add(1);

            // Calculate the middle elements of the row
            for (int j = 1; j < i; j++) {
                int a = previousRow.get(j - 1);
                int b = previousRow.get(j);
                level.add(a + b);
            }

            // Last element of each row is 1
            level.add(1);

            result.add(level);
        }
        
        return result;
    }
}
