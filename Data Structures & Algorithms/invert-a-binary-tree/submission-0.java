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
    public TreeNode invertTree(TreeNode root) {
       if(root == null) return root;
       root = invertTreeAux(root);
       return root;
    }
    private TreeNode invertTreeAux(TreeNode curr){
        if(curr == null){
            return curr;
        } else{
            TreeNode left = invertTreeAux(curr.left);
            TreeNode right = invertTreeAux(curr.right);
            curr.right = left;
            curr.left = right;
        }
        return curr;
    }
}


