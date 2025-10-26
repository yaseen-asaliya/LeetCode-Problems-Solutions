public class Solution {
    public int Rob(int[] nums) {
        int len = nums.Length;

        if(len == 0)
            return 0;
        
        if(len == 1)
            return nums[0];
        
        if(len == 2)
            return Math.Max(nums[0], nums[1]);
        
        if(len == 3)
            return Math.Max(nums[0], Math.Max(nums[1], nums[2]));

        return Math.Max(Helper(nums, 0, len-2), Helper(nums, 1, len-1));
    }

    private int Helper(int[] nums, int start, int end)
    {
        int prevMax =0 , currMax =0;

        for(int i = start; i<=end; i++)
        {
            int temp = Math.Max(currMax, prevMax+nums[i]);
            prevMax = currMax;
            currMax = temp;
        }

        return currMax;
    }
}