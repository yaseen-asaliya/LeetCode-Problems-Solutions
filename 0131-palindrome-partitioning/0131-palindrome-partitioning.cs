public class Solution {
    private IList<IList<string>> res;
    public IList<IList<string>> Partition(string s) {
        res = new List<IList<string>>();
        MakePartition(s, new List<string>());
        return res;
    }
    private void MakePartition(string s, List<string> lst)
    {
        if(s == null || s.Length == 0) {
            res.Add(new List<string>(lst));
            return;
        }

        for(int i=0;i<s.Length;i++)
        {
            string sub = s.Substring(0,i+1);
            if(!isPalindrome(sub)) continue;

            lst.Add(sub);
            MakePartition(s.Substring(i+1, s.Length-(i+1)) ,lst);
            lst.RemoveAt(lst.Count -1);
        }
    }
    private bool isPalindrome(string str)
    {
        int idx = str.Length -1;
        for(int i=0;i<str.Length/2;i++)
        {
            if(str[i] != str[idx--]) return false;
        }
        return true;
    }
}