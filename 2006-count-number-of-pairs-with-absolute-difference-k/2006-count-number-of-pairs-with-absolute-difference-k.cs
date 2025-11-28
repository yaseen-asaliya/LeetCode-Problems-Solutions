public class Solution {
    public int CountKDifference(int[] nums, int k) {
        var dic = new Dictionary<int, int>();
        int count = 0;
        
        foreach (int i in nums)
        {
            if (dic.ContainsKey(i - k))
                count += dic[i - k];
            if (dic.ContainsKey(i + k))
                count += dic[i + k];
            if (!dic.ContainsKey(i))
                dic.Add(i, 0);
            dic[i]++;
        }
        return count;
    }
}