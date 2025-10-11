public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> freq = new Dictionary<int, int>();
        int[] result = new int[k];

        for (int i=0;i<nums.Length;i++) {
            if (freq.ContainsKey(nums[i])) {
                freq[nums[i]] += 1;
            }
            else {
                freq[nums[i]] = 1;
            }
        }

        var sortedAsc = freq.OrderByDescending(kvp => kvp.Value);

        int index = 0;
        foreach (var kvp in sortedAsc)
        {
            if (index == k) {
                break;
            }
            result[index++] = kvp.Key;
        }

        return result;
    }
}