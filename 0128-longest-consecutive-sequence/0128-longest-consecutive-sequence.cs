public class Solution {
    public int LongestConsecutive(int[] nums) {
        if (nums.Length == 0) return 0;
        HashSet<int> set = new HashSet<int>(nums);
        int longest = 0;
        foreach (int num in set)  
        {
            if (!set.Contains(num - 1))  
            {
                int count = 1;
                int current = num;
                while (set.Contains(current + 1))
                {
                    count++;
                    current++;
                }
                longest = Math.Max(longest, count);
            }
        }
        return longest;
    }
}