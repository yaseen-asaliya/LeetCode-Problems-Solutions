public class Solution {
    private void Solve(List<string> ans, StringBuilder s, int open, int close, int n) {
        if (close == n && open == n) {
            ans.Add(s.ToString());
            return;
        }

        if (open < n) {
            s.Append('(');
            Solve(ans, s, open + 1, close, n);
            s.Length--;
        }

        if (close < open) {
            s.Append(')');
            Solve(ans, s, open, close + 1, n);
            s.Length--;
        }
    }

    public IList<string> GenerateParenthesis(int n) {
        var ans = new List<string>();
        var s = new StringBuilder();
        Solve(ans, s, 0, 0, n);
        return ans;
    }
}