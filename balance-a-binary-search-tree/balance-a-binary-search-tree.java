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
    private List<Integer> list;
    private void inorder(TreeNode root){
        if(root == null) return;
        inorder(root.left);
        list.add(root.val);
        inorder(root.right);   
    }
    
    private TreeNode balance(int left, int right){
        if(right<left) return null;
        else{
            int mid = left + (right - left)/2;
            TreeNode temp = new TreeNode(list.get(mid));
            temp.left = balance(left,mid-1);
            temp.right = balance(mid+1,right);
            return temp;
        }
    }
    
    public TreeNode balanceBST(TreeNode root) {
        list = new ArrayList<>();
        inorder(root);
        
        TreeNode temp = balance(0,list.size()-1);
        return temp;
    }
}