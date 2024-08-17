class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numMap = new HashSet<>();
        
        for (int num : nums){
            if (numMap.contains(num)) return true;
            else numMap.add(num);
        }
        return false;
    }
}