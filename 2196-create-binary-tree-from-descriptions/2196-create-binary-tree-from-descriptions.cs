public class Solution {
    public TreeNode CreateBinaryTree(int[][] descriptions)
    {
        var nodes = new Dictionary<int, TreeNode>();

        for (int i = 0; i < descriptions.Length; i++)
        {
            var parentVal = descriptions[i][0];

            if (!nodes.TryGetValue(parentVal, out TreeNode? parent))
            {
                parent = new(parentVal);
                nodes[parentVal] = parent;
            }

            var childVal = descriptions[i][1];

            if (!nodes.TryGetValue(childVal, out TreeNode? child))
            {
                child = new(childVal);
                nodes[childVal] = child;
            }

            if (descriptions[i][2] == 1)
                parent.left = child;
            else
                parent.right = child;
        }

        for (int i = 0; i < descriptions.Length; i++)
            nodes.Remove(descriptions[i][1]);

        return nodes.Single().Value;
    }
}