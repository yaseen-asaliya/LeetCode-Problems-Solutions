public class Solution {
    public int SmallestRangeI(int[] nums, int k) {
        int maxNum = nums[0];
        int minNum = nums[0];

        for(int i=0;i<nums.Length;i++){
            if (nums[i] > maxNum)
                maxNum = nums[i];

            if (nums[i] < minNum)
                minNum = nums[i];
        }

        int result = maxNum - minNum - 2 * k;
        return result > 0 ? result : 0;
    }
}