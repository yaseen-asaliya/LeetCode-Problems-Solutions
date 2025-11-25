public class Solution
{
    private int ReverseInt(int num)
    {
        int rev = 0;

        while (num > 0)
        {
            rev = rev * 10 + (num % 10);
            num /= 10;
        }

        return rev;
    }

    public int CountDistinctIntegers(int[] nums)
    {
        HashSet<int> st = new HashSet<int>();

        foreach (int n in nums)
        {
            st.Add(n);              
            st.Add(ReverseInt(n));  
        }

        return st.Count;
    }
}
