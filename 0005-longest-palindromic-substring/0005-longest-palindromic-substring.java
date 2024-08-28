class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }

        int resLen = 0;
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Odd-length palindrome
            int l = i, r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > resLen) {
                    resLen = r - l + 1;
                    start = l;
                    end = r;
                }
                l--;
                r++;
            }
            
            // Even-length palindrome
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > resLen) {
                    resLen = r - l + 1;
                    start = l;
                    end = r;
                }
                l--;
                r++;
            }
        }
        
        return s.substring(start, end + 1);
    }
}
