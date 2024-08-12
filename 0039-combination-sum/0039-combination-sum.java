import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        helper(0, candidates, target, result, new ArrayList<>());
        return result;
    }
    
    private void helper(int index, int[] candidates, int target, List<List<Integer>> result, List<Integer> path) {
        // Base Case: If target is 0, add the current path to the result
        if (target == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        
        // If target is negative or index is out of bounds, stop recursion
        if (target < 0 || index >= candidates.length) {
            return;
        }
        
        // Include the current candidate
        path.add(candidates[index]);
        // Recurse with the same index to allow repeated use of the current candidate
        helper(index, candidates, target - candidates[index], result, path);
        // Backtrack: remove the last added element
        path.remove(path.size() - 1);
        
        // Exclude the current candidate and move to the next index
        helper(index + 1, candidates, target, result, path);
    }
}
