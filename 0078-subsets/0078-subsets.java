import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        generateSubsets(0, new ArrayList<>(), result, nums);
        return result;
    }
    
    private void generateSubsets(int index, List<Integer> path, List<List<Integer>> result, int[] nums) {
        // Base Case: When all elements are processed, add the current subset to the result
        if (index == nums.length) {
            result.add(new ArrayList<>(path)); // Add a copy of the current path
            return;
        }
        
        // Exclude the current element
        generateSubsets(index + 1, path, result, nums);
        
        // Include the current element
        path.add(nums[index]);
        generateSubsets(index + 1, path, result, nums);
        
        // Backtrack to remove the last added element for further exploration
        path.remove(path.size() - 1);
    }
}
