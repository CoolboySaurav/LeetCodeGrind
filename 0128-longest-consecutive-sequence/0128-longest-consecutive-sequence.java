import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestConsecutive(int[] nums) {
        // Create a HashSet and add all elements from nums
        Set<Integer> numberSet = new HashSet<>();
        for (int num : nums) {
            numberSet.add(num);
        }

        int maxLen = 0;

        // Iterate through each number in the array
        for (int num : nums) {
            // Check if it's the start of a sequence
            if (!numberSet.contains(num - 1)) {
                int currentNum = num;
                int currentLen = 1;

                // Find the length of the sequence
                while (numberSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentLen++;
                }

                // Update maxLen if necessary
                maxLen = Math.max(maxLen, currentLen);
            }
        }

        return maxLen;
    }
}
