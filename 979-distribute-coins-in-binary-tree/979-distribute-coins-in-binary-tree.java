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
    int numMoves;
    public int distributeCoins(TreeNode root) {
        if(root==null) {
            return 0;
        }
        
        numMoves = 0;
        helper(root);
        return numMoves;
        
    }
    
    private int helper(TreeNode root) {
        if(root==null) {
            return 0;
        }
        
        int left = helper(root.left);
        int right = helper(root.right);
        
        numMoves += Math.abs(left) + Math.abs(right);
        
        return root.val -1 + left + right;
    }
}