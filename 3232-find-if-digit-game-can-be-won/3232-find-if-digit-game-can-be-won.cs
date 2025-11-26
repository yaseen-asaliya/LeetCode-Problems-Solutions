public class Solution {
    public bool CanAliceWin(int[] nums) {
        int sumSingle = 0;
        int sumDouble = 0;

        foreach (int num in nums) {
            if (num <= 9)
                sumSingle += num;
            else
                sumDouble += num;
        }

        bool aliceSingleWins = sumSingle > sumDouble;

        bool aliceDoubleWins = sumDouble > sumSingle;

        return aliceSingleWins || aliceDoubleWins;
    }
}
