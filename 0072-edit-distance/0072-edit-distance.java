class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] prev = new int[n + 1];
        
        for (int i = 0; i < n + 1; i++){
            prev[i] = i;
        }
        
        for (int i = 1; i < m + 1; i++){
            int[] cur = new int[n + 1];
            cur[0] = i;
            for (int j = 1; j < n + 1; j++){
                if (word1.charAt(i - 1) == word2.charAt(j - 1)){
                    cur[j] = prev[j - 1];
                }
                else{
                    int insert = cur[j - 1];
                    int delete = prev[j];
                    int replace = prev[j - 1];
                    cur[j] = 1 + Math.min(insert, Math.min(delete, replace));
                }
            }
            prev = cur;
        }
        
        return prev[n];
    }
}