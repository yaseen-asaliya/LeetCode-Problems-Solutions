public class MinStack
{
    private List<int> st;
    private List<int> minStack;

    public MinStack()
    {
        st = new List<int>();
        minStack = new List<int>();
    }

    public void Push(int val)
    {
        st.Add(val);

        if (minStack.Count == 0 || val <= minStack[minStack.Count - 1])
        {
            minStack.Add(val);
        }
    }

    public void Pop()
    {
        if (st.Count == 0)
            return;

        int top = st[st.Count - 1];
        st.RemoveAt(st.Count - 1);

        if (top == minStack[minStack.Count - 1])
        {
            minStack.RemoveAt(minStack.Count - 1);
        }
    }

    public int Top()
    {
        return st[st.Count - 1];
    }

    public int GetMin()
    {
        return minStack[minStack.Count - 1];
    }
}
