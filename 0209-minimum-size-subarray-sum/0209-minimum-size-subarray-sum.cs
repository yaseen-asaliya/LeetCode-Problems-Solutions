public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0;
        int sum = 0;
        int ans = int.MaxValue;

        while (right < nums.Length) {
            sum += nums[right];

            while (sum >= target) {
                ans = Math.Min(ans, right - left + 1);
                sum -= nums[left];
                left++;
            }

            right++;
        }

        return ans == int.MaxValue ? 0 : ans;
    }
}
