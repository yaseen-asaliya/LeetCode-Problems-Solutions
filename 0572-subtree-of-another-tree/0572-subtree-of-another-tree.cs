/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private string Serialize(TreeNode node) {
        if (node == null) {
            return "N";
        }
        return "(" + node.val + "," + Serialize(node.left) + "," + Serialize(node.right) + ")";
    }

    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        string rootSerialized = Serialize(root);
        string subRootSerialized = Serialize(subRoot);
        return rootSerialized.Contains(subRootSerialized);
    }
}