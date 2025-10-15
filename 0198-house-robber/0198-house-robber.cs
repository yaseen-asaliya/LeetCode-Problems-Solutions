public class Solution {
    public int Rob(int[] nums) {
        if (nums == null || nums.Length == 0) {
            return 0;
        }
        if (nums.Length == 1) {
            return nums[0];
        }

        int prevPrev = nums[0];
        int prev = Math.Max(nums[0], nums[1]);

        for (int i = 2; i < nums.Length; ++i) {
            int current = Math.Max(prevPrev + nums[i], prev);
            prevPrev = prev;
            prev = current;
        }

        return prev;
    }
}