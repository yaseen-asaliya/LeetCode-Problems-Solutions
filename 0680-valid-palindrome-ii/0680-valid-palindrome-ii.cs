public class Solution {
    public bool ValidPalindrome(string s) {
        int left = 0, right = s.Length - 1;
        
        while (left < right){
            if (s[left] != s[right])
                return IsPalindrome(s, left, right-1) || IsPalindrome(s, left+1, right);

            left++; right--;
        }

        return true;
    }

    private bool IsPalindrome(string s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++; right--;
        }
        return true;
    }
}