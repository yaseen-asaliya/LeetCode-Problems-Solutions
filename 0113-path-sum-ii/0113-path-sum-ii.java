/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void sum(TreeNode root, int sum, int targetSum, List<Integer> tmp, List<List<Integer>> res){
        sum+= root.val;
        tmp.add(root.val);

        if(sum == targetSum && root.left == null && root.right == null){
           res.add(new ArrayList<>(tmp));
        }

        if(root.left != null){
            sum(root.left, sum, targetSum, tmp, res);
            tmp.remove(tmp.size() - 1);
        }

        if(root.right != null){
            sum(root.right, sum, targetSum, tmp, res);
            tmp.remove(tmp.size() - 1);
        }
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<>();;

        if(root!=null){
            sum(root, 0, targetSum, new ArrayList(), res);
        }
        return res;
    }
}