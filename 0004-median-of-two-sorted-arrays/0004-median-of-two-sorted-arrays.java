class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m > n) return findMedianSortedArrays(nums2, nums1); // Ensure nums1 is the smaller array
        
        int l = 0, r = m;
        int halfLen = (m + n + 1) / 2; // This is the length of the left half of the merged array
        
        while (l <= r) {
            int mid1 = l + (r - l) / 2; // Midpoint for nums1
            int mid2 = halfLen - mid1; // Corresponding midpoint for nums2
            
            int l1 = (mid1 == 0) ? Integer.MIN_VALUE : nums1[mid1 - 1]; // Left of nums1
            int r1 = (mid1 == m) ? Integer.MAX_VALUE : nums1[mid1]; // Right of nums1
            int l2 = (mid2 == 0) ? Integer.MIN_VALUE : nums2[mid2 - 1]; // Left of nums2
            int r2 = (mid2 == n) ? Integer.MAX_VALUE : nums2[mid2]; // Right of nums2
            
            if (l1 <= r2 && l2 <= r1) {
                if ((m + n) % 2 == 0) {
                    // Even total length
                    return (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
                } else {
                    // Odd total length
                    return Math.max(l1, l2);
                }
            } else if (l1 > r2) {
                // `nums1[mid1]` is too large, reduce `mid1`
                r = mid1 - 1;
            } else {
                // `nums2[mid2]` is too large, increase `mid1`
                l = mid1 + 1;
            }
        }
        return 0;
    }
}
