class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<Integer> nums = new ArrayList<>();
        
        for (int i = 1; i < 10; i++){
            nums.add(i);
        }
        List<List<Integer>> result = new ArrayList<>();
        helper(0, nums, result, n, k, new ArrayList<>());
        return result;
    }
    
    private void helper(int index, List<Integer> nums, List<List<Integer>> result, int n, int k, List<Integer> path){
        // Base Case
        if ((k == 0) & (n == 0)){
            result.add(new ArrayList<>(path));
            return;
        }
        if ((k < 0) || (n < 0) || (index >= nums.size())) return;
        
        // Pick case
        path.add(nums.get(index));
        helper(index + 1, nums, result, n - nums.get(index), k - 1, path);
        path.remove(path.size() - 1);
        // Not Pick case
        helper(index + 1, nums, result, n, k, path);
    }
}