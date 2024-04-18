class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0, left = 0, right = height.length - 1;

        while(left < right){
            int width = right - left;
            int h = Math.min(height[left],height[right]);
            int area = width * h;
            maxArea=(Math.max(area,maxArea));
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}