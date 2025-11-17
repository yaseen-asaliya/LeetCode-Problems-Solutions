public class Solution {
    public string LargestGoodInteger(string num) {
        string res = "";

        for(int i=0;i<num.Length-2;i++) {
            if (num[i] == num[i+1] && num[i+1] == num[i+2]) {
                if ((i + 3 < num.Length - 1 && num[i] != num[i+3]) || num.Length == 3)
                    res = num[i].ToString() + num[i+1].ToString() + num[i+2].ToString();
            }
        }

        return res;
    }
}