class Solution {
    public int trap(int[] height) {
        int maxleft = -1, maxright = -1;
        int water = 0;
        int l = 0, r = height.length - 1;
        
        while (l <= r){
            maxleft = Math.max(maxleft, height[l]);
            water += maxleft - height[l];
            
            maxright = Math.max(maxright, height[r]);
            water += maxright - height[r];
            
            if (maxleft < maxright) l++;
            else r--;
        }
        return water;
        
    }
}