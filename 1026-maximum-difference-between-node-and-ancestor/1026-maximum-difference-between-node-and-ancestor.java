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
    
public int maxAncestorDiff(TreeNode root) {
    return Math.max(helper(root.left, root.val, root.val), 
                    helper(root.right, root.val, root.val));
}

public int helper(TreeNode node, int maxPrev, int minPrev){
    
    if(node==null){
        return Integer.MIN_VALUE;
    }
    
    int diff= Math.max(Math.abs(maxPrev-node.val),Math.abs(minPrev-node.val));
    
    maxPrev= Math.max(maxPrev, node.val);
    minPrev= Math.min(minPrev,node.val);
    
    return Math.max(diff,Math.max(helper(node.left,maxPrev,minPrev),
                                  helper(node.right,maxPrev,minPrev)));
}
    
    
}