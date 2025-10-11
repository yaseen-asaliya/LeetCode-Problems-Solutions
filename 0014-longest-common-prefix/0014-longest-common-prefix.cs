public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string Res = "";

        if (strs.Length == 0) return "";        
        if (strs[0].Length == 0) return "";      

        int c = 0;                         
        int index = 0;                         
        char currentChar = strs[0][0];            

        while (true) {
            if (c >= strs[index].Length || strs[index][c] != currentChar) {
                break;                        
            }

            index++;

            if (index == strs.Length) {       
                Res += currentChar;             
                c++;                              

                if (c >= strs[0].Length) break; 

                currentChar = strs[0][c];        
                index = 0;                   
            }
        }

        return Res;
    }
}
