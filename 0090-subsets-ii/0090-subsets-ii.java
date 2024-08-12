class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        helper(0, new ArrayList<>(), result, nums);
        return  result;
    }
    
    private void helper(int index, List<Integer> path, List<List<Integer>> result, int[] nums){
        //Base Case
        result.add(new ArrayList<>(path));
        
        for (int i = index; i < nums.length; i++){
            if ((i > index) && (nums[i] == nums[i - 1])) continue;
            path.add(nums[i]);
            helper(i + 1, path, result, nums);
            path.remove(path.size()  - 1);
        }
    }
}