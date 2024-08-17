class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] charArray = new int[26];  // Array to count character frequencies
        
        for (int i = 0; i < s.length(); i++) {
            // Increase count for the character in string s
            int ind = s.charAt(i) - 'a';
            charArray[ind]++;
            
            // Decrease count for the character in string t
            ind = t.charAt(i) - 'a';
            charArray[ind]--;
        }
        
        // Check if all counts are zero
        for (int count : charArray) {
            if (count != 0) return false;
        }
        
        return true;
    }
}
