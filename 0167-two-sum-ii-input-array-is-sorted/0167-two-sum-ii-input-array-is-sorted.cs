public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int p1=0, p2= numbers.Length-1;
        int[] res = new int[2];

        while (p1 <= p2) {
            if (numbers[p1] + numbers[p2] == target) {
                res[0] = p1 + 1;
                res[1] = p2 + 1;
                break;
            }
            else if (numbers[p1] + numbers[p2] > target) {
                p2--;
            }
            else {
                p1++;
            }
        }
        return res;
    }
}