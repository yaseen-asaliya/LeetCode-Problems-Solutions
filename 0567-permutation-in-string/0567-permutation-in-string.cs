public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length)
            return false;

        Dictionary<char, int> s1Count = new Dictionary<char, int>();
        foreach (char c in s1) {
            if (s1Count.ContainsKey(c)) s1Count[c]++;
            else s1Count[c] = 1;
        }

        Dictionary<char, int> s2Count = new Dictionary<char, int>();
        int windowSize = s1.Length;

        for (int i = 0; i < s2.Length; i++) {
            char c = s2[i];
            if (s2Count.ContainsKey(c)) s2Count[c]++;
            else s2Count[c] = 1;

            if (i >= windowSize) {
                char leftChar = s2[i - windowSize];
                s2Count[leftChar]--;
                if (s2Count[leftChar] == 0)
                    s2Count.Remove(leftChar);
            }

            if (AreDictionariesEqual(s1Count, s2Count))
                return true;
        }

        return false;
    }

    private bool AreDictionariesEqual(Dictionary<char, int> d1, Dictionary<char, int> d2) {
        if (d1.Count != d2.Count)
            return false;

        foreach (var kvp in d1) {
            if (!d2.ContainsKey(kvp.Key) || d2[kvp.Key] != kvp.Value)
                return false;
        }

        return true;
    }
}
