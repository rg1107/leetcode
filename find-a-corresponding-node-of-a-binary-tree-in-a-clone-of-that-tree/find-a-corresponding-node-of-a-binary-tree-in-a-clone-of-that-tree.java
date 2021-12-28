/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        
        q1.add(original);
        q2.add(cloned);
        
        while(!q1.isEmpty()) {
            TreeNode temp = q1.poll();
            TreeNode temp1 = q2.poll();
            
            if(temp == target){
                return temp1;
            }
            
            if(temp.left!=null) {
                q1.add(temp.left);
                q2.add(temp1.left);
            }
            if(temp.right!=null) {
                q1.add(temp.right);
                q2.add(temp1.right);
            }
        }
        
        return null;
        
    }
    
}