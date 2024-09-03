class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sum = 0;
        int n = gas.length;
        for (int i = 0; i < n; i++){
            sum += gas[i] - cost[i];
        }
        if (sum < 0) return -1;
        
        int res = 0;
        sum = 0;
        
        for (int i = 0; i < n; i++){
            sum += gas[i] - cost[i];
            if (sum < 0){
                res = i + 1;
                sum = 0;
            }
        }
        return res;
    }
}