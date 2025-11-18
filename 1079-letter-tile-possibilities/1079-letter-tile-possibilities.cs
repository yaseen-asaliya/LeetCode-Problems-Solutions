public class Solution {
    public int NumTilePossibilities(string tiles) {
        var counts = new int[26];
        foreach (var ch in tiles)
            counts[ch - 'A']++;

        return DFS(counts);
    }

    private int DFS(int[] counts)
    {
        var sum = 0;
        for (int i = 0; i < 26; i++)
        {
            if (counts[i] == 0) continue;

            sum++;
            counts[i]--;
            sum += DFS(counts);
            counts[i]++;
        }

      return sum;
    }
}