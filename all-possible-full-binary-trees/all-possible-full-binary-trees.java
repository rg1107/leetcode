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
    Map<Integer, List<TreeNode>> dp = new HashMap();
    public List<TreeNode> allPossibleFBT(int n) {
        if(n==1){
            List<TreeNode> tree = new ArrayList();
            tree.add(new TreeNode(0));
            
            return tree; 
        }
        
        if(dp.containsKey(n)) return dp.get(n);
        
        List<TreeNode> ans = new ArrayList();
        
        for(int i = 1; i<n; i+=1){
            List<TreeNode> right = allPossibleFBT(n-1-i);
            List<TreeNode> left = allPossibleFBT(i);
            
            for(TreeNode leftNode: left){
                for(TreeNode rightNode: right){
                    TreeNode root = new TreeNode(0);
                    
                    root.left = leftNode;
                    root.right = rightNode;
                    
                    ans.add(root);
                }
            }
        }
        
        dp.put(n, ans);
        return ans;
    }
    
}