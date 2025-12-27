public class Solution {
    public IList<string> LetterCasePermutation(string s) {
        void Permute(char[] temp, int index, IList<string> result)
        {
            if (index == temp.Length)
            {
                result.Add(new string(temp));
                return;
            }

            Permute(temp, index + 1, result);

            if (char.IsLetter(temp[index]))
            {
                temp[index] = char.IsLower(temp[index]) ? char.ToUpper(temp[index]) : char.ToLower(temp[index]);
                Permute(temp, index + 1, result);
            }
        }

        var result = new List<string>();

        Permute(s.ToCharArray(), 0, result);

        return result;
    }
}