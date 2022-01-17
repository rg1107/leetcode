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
class FindElements {
    
    TreeNode res;

    public FindElements(TreeNode root) {
        this.res = root;
    }
    
    public boolean find(int target) {
        return helper(res, target, 0);
    }
    
    private boolean helper(TreeNode root, int target, int curr) {
        if(root==null) {
            return false;
        }
        
        if(target==curr) {
            return true;
        }
        
        return helper(root.left, target, curr*2 +1) || helper(root.right, target, curr*2 +2);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */