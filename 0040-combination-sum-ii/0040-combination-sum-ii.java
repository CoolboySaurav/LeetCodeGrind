class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        
        List<List<Integer>> result = new ArrayList<>();
        helper(0, candidates, new ArrayList<>(), result, target);
        return result;
    }
    
    private void helper(int index, int[] candidates, List<Integer> path, List<List<Integer>> result, int target){
        // Base Case
        if (target == 0){
            result.add(new ArrayList<>(path));
            return;
        }
        if ((target < 0) || (index >= candidates.length)){
            return;
        }
        
        for (int i = index; i < candidates.length; i++){
            if ((i > index) && (candidates[i] == candidates[i - 1])) continue;
            path.add(candidates[i]);
            helper(i + 1, candidates, path, result, target - candidates[i]);
            path.remove(path.size() - 1);
        }
    }
}