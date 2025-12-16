public class Solution {
    public int HammingDistance(int x, int y) {
        string bi = Convert.ToString(x ^ y, 2);
        
        int count = 0;
        foreach(char ch in bi){
            if(ch== '1'){
                count++;
            }
        }
        return count;
    }
}