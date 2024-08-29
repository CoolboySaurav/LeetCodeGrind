import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // Sort both arrays to facilitate greedy matching
        Arrays.sort(g);
        Arrays.sort(s);
        
        int count = 0; // Counter for the number of content children
        int l = g.length - 1; // Pointer for the greed factor array
        int r = s.length - 1; // Pointer for the cookie size array
        
        // Traverse from the largest greed factor and largest cookie size
        while (l >= 0 && r >= 0) {
            // If the current cookie can satisfy the current child's greed
            if (g[l] <= s[r]) {
                count++; // Increment the count
                r--; // Move to the next largest cookie
            }
            l--; // Move to the next largest greed factor
        }
        
        return count; // Return the number of content children
    }
}
