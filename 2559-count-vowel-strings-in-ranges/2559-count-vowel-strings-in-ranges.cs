public class Solution {
    public int[] VowelStrings(string[] words, int[][] queries) {
        int[] ans = new int[queries.Length];
        int[] temp = new int[words.Length];
        int tot = 0;
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };

        for(int i=0;i<words.Length;i++) {
            if (vowels.Contains(words[i][0])) {
                if (vowels.Contains(words[i][words[i].Length - 1]))
                    temp[i] = 1;
                    continue;
            }
            temp[i] = 0;
        }

        for(int i=0;i<queries.Length;i++){
            for(int j= queries[i][0];j<=queries[i][1];j++){
                tot += temp[j];
            }
            ans[i] = tot;
            tot = 0;
        }

        return ans;
    }
}