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
import java.util.*;

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> list = new ArrayList<>();
        traverse(root, list);
        Collections.sort(list);
        return list.get(k - 1);
    }

    private void traverse(TreeNode ptr, ArrayList<Integer> list) {
        if (ptr == null) return;
        list.add(ptr.val);
        traverse(ptr.left, list);
        traverse(ptr.right, list);
    }
}
