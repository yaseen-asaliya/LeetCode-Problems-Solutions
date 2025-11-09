public class Solution {
    public int[] ReplaceElements(int[] arr) {
        Stack<int> s = [];
        var max = -1;

        for (int i = arr.Length; i > 0; i--)
        {
            max = i == arr.Length ? -1 : Math.Max(arr[i], max);
            s.Push(max);
        }

        var ans = new int[arr.Length];
        
        for (int i = 0; i < ans.Length; i++)
            ans[i] = s.Pop();

        return ans;
    }
}