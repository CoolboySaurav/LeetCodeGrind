class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n1 = text1.length(), n2 = text2.length();
        int[] prev = new int[n2 + 1];
        
        for (int i = 1; i < n1 + 1; i++){
            int[] cur = new int[n2 + 1];
            for (int j = 1; j < n2 + 1; j++){
                if (text1.charAt(i - 1) == text2.charAt(j - 1)){
                    cur[j] = 1 + prev[j - 1];
                }
                else{
                    cur[j] = Math.max(cur[j - 1], prev[j]);
                }
            }
            prev = cur;
        }
        
        return prev[n2];
    }
}