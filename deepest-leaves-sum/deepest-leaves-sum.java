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
    public int deepestLeavesSum(TreeNode root) {
        
        Queue<TreeNode> q = new LinkedList<>();
        int sum = 0;
        q.offer(root);
        q.offer(null);
        
        while(!q.isEmpty()) {
            TreeNode temp = q.remove();
            if(temp==null){
                if(!q.isEmpty()) {
                    sum = 0;
                    q.offer(null);
                }
                continue;
            }
            sum = sum + temp.val;
            if(temp.left!=null){
                q.offer(temp.left);
            }
            if(temp.right!=null) {
                q.offer(temp.right);
            }
        }
        
        return sum;
    }
}