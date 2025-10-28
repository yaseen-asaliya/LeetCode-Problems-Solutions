public class Solution {
    public int FindMin(int[] nums) {
        int l = 0, r = nums.Length - 1;
        int minValue = nums[0];

        while (l <= r) {
            int mid = r + l / 2;
            minValue = Math.Min(minValue, nums[mid]);

            if (nums[mid] >= nums[l]) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }
        return minValue;
    }
}