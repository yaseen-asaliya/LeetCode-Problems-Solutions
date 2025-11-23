public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        var i = 0;
        var j = 0;
        var stack = new Stack<int>();
        while (j < popped.Length)
        {
            if (stack.Any() && stack.Peek() == popped[j])
            {
                stack.Pop();
                j++;
                continue;
            }

            if (i < pushed.Length)
            {
                stack.Push(pushed[i]);
                i++;
                continue;
            }

            return false;
        }

        return true;
    }
}

