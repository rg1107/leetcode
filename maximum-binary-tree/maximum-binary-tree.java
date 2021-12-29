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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        
        return helper(nums, 0, nums.length-1);
        
    }
    
    public TreeNode helper(int[] nums, int l, int r) {
        if(l>r){
            return null;
        }
        int max = nums[l], ind = l;
        for(int i =l;i<=r;i++){
            if(nums[i]>max){
                max = nums[i];
                ind = i;
            }
        }
        
        TreeNode root = new TreeNode(max);
        root.left = helper(nums, l, ind-1);
        root.right = helper(nums, ind+1, r);
        
        return root;
    }
}