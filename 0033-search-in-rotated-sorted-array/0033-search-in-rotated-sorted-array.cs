public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length - 1;


        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target){
                return mid;
            }
            if (nums[l] <= nums[mid]) {
                if (target > nums[mid] || target < nums[l]){
                    l = mid + 1;
                }
                else {
                    r = mid - 1;
                }
            }
            else {
                if (target < nums[mid] || target > nums[r]){
                    r = mid - 1;
                }
                else {
                    l = mid + 1;
                }
            }
        }

        return -1;
    }
}